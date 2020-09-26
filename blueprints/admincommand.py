from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         CommandsFilter,
                         TextFilter
                         )

from blueprints.services.dbsystem import change_await_message
from utils.constants import MENU_KB

admin_router = DefaultRouter()


@simple_bot_message_handler(admin_router, PayloadFilter({"command": "add_group"}))
async def add_group(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    await change_await_message(user_id=user_id, await_value=301)
    return await event.answer(
        message="ввидите название и юрл группы "
    )