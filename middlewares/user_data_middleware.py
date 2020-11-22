from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult, SimpleBotEvent

from blueprints.registration import new_university, offer_to_register
from blueprints.services.dbsystem import create_user, ActiveUser
import logging


class UserEnterMiddleware(BaseMiddleware):
    async def pre_process_event(self, event: SimpleBotEvent) -> MiddlewareResult:
        if event.object.type == 'message_typing_state':
            logging.info('Игнорирование события')
            return MiddlewareResult(False)
        if event.object.type == 'message_reply':
            logging.info("Сообщение отправлено пользователю ")
        else:
            user_id = event.object.object.message.from_id
            Usr = ActiveUser(user_id)
            if not hasattr(Usr, "first_name"):
                user_data = await event.api_ctx.users.get(user_ids=user_id)
                await create_user(user_id=user_id, first_name=user_data.response[0].first_name,
                                  last_name=user_data.response[0].last_name)
                Usr = ActiveUser(user_id)
                if Usr.first_name is not None:
                    logging.info('Пользователь' + str(Usr.first_name) + " " +
                                 str(Usr.last_name) + " успешно создан")
                else:
                    logging.info('Ошибка при создание пользователя')
                    return MiddlewareResult(False)
                await offer_to_register(event=event, user_id=user_id)
            if Usr.university_id is None:
                await offer_to_register(event=event, user_id=user_id)
                return MiddlewareResult(False)
            logging.info('Middleware был пройден пользователем ' + str(Usr.first_name) + ' ' + str(Usr.last_name))
            return MiddlewareResult(True)
