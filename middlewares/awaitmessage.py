from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult
from blueprints.dbsistem import gey_await_message, change_await_message, get_group_url
import logging


class AwaitMiddleware(BaseMiddleware):
    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        user_id = event.object.object.message.from_id
        await_message = gey_await_message(user_id=user_id)
        if await_message != 0:
            if await_message == 201:
                await get_group_url(group_id=event.object.object.text)
                await change_await_message(user_id=user_id, await_value=0)
        logging.debug("Await Middleware был пройден")
        return MiddlewareResult(True)

