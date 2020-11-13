from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         CommandsFilter,
                         TextFilter
                         )

from blueprints.services.dbsystem import ActiveUser
from utils.constants import MENU_KB

admin_router = DefaultRouter()


@simple_bot_message_handler(admin_router, PayloadFilter({"command": "add_group"}))
async def add_group(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    Usr = ActiveUser(id=user_id)
    Usr.await_message = 301
    await Usr.change_await_message()
    return await event.answer(
        message="ввидите название и юрл группы "
    )