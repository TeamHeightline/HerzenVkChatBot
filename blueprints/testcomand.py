from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         TextFilter
                         )

from utils.constants import MENU_KB, TEST_KB

test_router = DefaultRouter()


@simple_bot_message_handler(test_router, TextFilter(text="начать", ignore_case=True))
async def first_message_to_bot(event: SimpleBotEvent):
    return await event.answer(
        message="Добро пожаловаь, здесь будет собрана вся важная информация и расписание занятий",
        keyboard=MENU_KB.get_keyboard()
    )


@simple_bot_message_handler(test_router, PayloadFilter({"command": "начать"}))
async def first_message_to_bot_payload(event: SimpleBotEvent):
    return await event.answer(
        message="Добро пожаловаь, здесь будет собрана вся важная информация и расписание занятий",
        keyboard=MENU_KB.get_keyboard()
    )


@simple_bot_message_handler(test_router, TextFilter("!"))
async def test_keyboard_dropper(event: SimpleBotEvent):
    return await event.answer(
        message="Клавиатура для тестов",
        keyboard=TEST_KB.get_keyboard()
    )



