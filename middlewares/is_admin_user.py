from blueprints.models import *
from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult
from blueprints.dbsistem import is_user_admin


class IsUserAdminMiddleware(BaseMiddleware):
    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        user_id = event.object.object.message.from_id
        r = is_user_admin(user_id=user_id)
        if r is not None:
            return MiddlewareResult(True)
