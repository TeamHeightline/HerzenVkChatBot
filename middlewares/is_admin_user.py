from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult
import logging


class IsUserAdminMiddleware(BaseMiddleware):
    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        # user_id = event.object.object.message.from_id
        # r = is_user_admin(user_id=user_id)
        # if r is not None:
        logging.info("Admin middleware start")
        return MiddlewareResult(False)
