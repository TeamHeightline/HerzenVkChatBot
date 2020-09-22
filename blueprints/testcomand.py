from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         TextFilter
                         )

from utils.constants import MENU_KB, TEST_KB
from blueprints.services.dbsystem import change_await_message, get_group_url

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


@simple_bot_message_handler(test_router, TextFilter("111"))
async def test(event: SimpleBotEvent):
    await change_await_message(user_id=494639302, await_value=100)
    return await event.answer(
        message="Test passed",
        keyboard=MENU_KB.get_keyboard()
    )


@simple_bot_message_handler(test_router, TextFilter("get url"))
async def test_group_url(event: SimpleBotEvent):
    r = await get_group_url(group_id=0)
    return await event.answer(
        message="Group url:" + str(r),
        keyboard=MENU_KB.get_keyboard()
    )


@simple_bot_message_handler(test_router, TextFilter("!"))
async def test_keyboard_dropper(event: SimpleBotEvent):
    return await event.answer(
        message="Клавиатура для тестов",
        keyboard=TEST_KB.get_keyboard()
    )


@simple_bot_message_handler(test_router, PayloadFilter({"command": "prepare to get group id"}))
async def first_message_to_bot_payload(event: SimpleBotEvent):
    await change_await_message(user_id=event.object.object.message.from_id, await_value=201)
    return await event.answer(
        message="Введите айди вашей группы",
        keyboard=MENU_KB.get_keyboard()
    )