from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         CommandsFilter,
                         TextFilter
                         )
from utils.constants import MENU_KB
test_router = DefaultRouter()


@simple_bot_message_handler(test_router, TextFilter("111"))
async def test(event: SimpleBotEvent):
    return await event.answer(
        message="Test passed",
        keyboard=MENU_KB.get_keyboard()
    )
