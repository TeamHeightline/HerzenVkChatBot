from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         CommandsFilter,
                         TextFilter
                         )
from utils.constants import MENU_KB
from .dbsistem import change_await_message

test_router = DefaultRouter()


@simple_bot_message_handler(test_router, TextFilter(text="начать", ignore_case=True))
async def first_message_to_bot(event: SimpleBotEvent):
    return await event.answer(
        message="Добро пожаловаь, здесь будет собрана вся важная информация и расписание занятий",
        keyboard=MENU_KB.get_keyboard()
    )


@simple_bot_message_handler(test_router, TextFilter("111"))
async def test(event: SimpleBotEvent):
    print("мы туть)")
    await change_await_message(user_id=494639302, await_value=100)
    return await event.answer(
        message="Test passed",
        keyboard=MENU_KB.get_keyboard()
    )
