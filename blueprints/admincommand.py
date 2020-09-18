from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         CommandsFilter,
                         TextFilter
                         )
from utils.constants import MENU_KB

admin_router = DefaultRouter()


@simple_bot_message_handler(admin_router, PayloadFilter({"command": "add_group"}))
async def add_group():
    pass
