from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         TextFilter,
RegexFilter
                         )

from blueprints.dbsistem import change_await_message, get_group_url, gey_await_message
from utils.constants import MENU_KB
import logging

await_router = DefaultRouter()

# user_id = event.object.object.message.from_id
# await_message = await gey_await_message(user_id=user_id)
# if await_message != 0:
#     if await_message == 201:
#         r = await get_group_url(group_id=event.object.object.message.text)
#         print(r)
#         await change_await_message(user_id=user_id, await_value=0)
# logging.debug("Await Middleware был пройден")
# return MiddlewareResult(True)


@simple_bot_message_handler(await_router, RegexFilter(r"\d+"))
async def await_message_processor(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    await_message = await gey_await_message(user_id=user_id)
    if await_message != 0:
        if await_message == 201:
            r = await get_group_url(group_id=event.object.object.message.text)
            print(r)
            await change_await_message(user_id=user_id, await_value=0)
            logging.debug("Group url received")
            return await event.answer(
                message=r,
                keyboard=MENU_KB.get_keyboard()
            )