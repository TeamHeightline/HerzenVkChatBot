from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult
from blueprints.services.dbsystem import get_user, create_user
import logging


class UserEnterMiddleware(BaseMiddleware):
    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        user_id = event.object.object.message.from_id

        user_first_name, user_last_name = await get_user(user_id=user_id)

        if user_first_name is None:
            user_data = await event.api_ctx.users.get(user_ids=user_id)
            await create_user(user_id=user_id, first_name=user_data.response[0].first_name,
                              last_name=user_data.response[0].last_name)

            user_first_name, user_last_name = await get_user(user_id=user_id)
            if user_first_name is not None:
                logging.info('Пользователь' + str(user_first_name) + " " +
                             str(user_last_name) + " успешно создан")
            else:
                logging.info('Ошибка при создание пользователя')
                return MiddlewareResult(False)
        logging.info('Middleware был пройден пользователем ' + str(user_first_name) + ' ' + str(user_last_name))
        return MiddlewareResult(True)
