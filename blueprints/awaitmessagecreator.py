from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         RegexFilter
                         )

from blueprints.services.dbsystem import change_await_message, get_group_url, gey_await_message, get_level_id, \
    get_university_group_list
from utils.constants import MENU_KB
import logging
from blueprints.services.api import get_timetable
from .services.dbsystem import add_group
await_router = DefaultRouter()


#
# 201 - возвращение расписания по урлу
# 301 - создание групы
@simple_bot_message_handler(await_router, RegexFilter(r"."))
async def await_message_processor(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    await_message = await gey_await_message(user_id=user_id)
    print(await_message)
    if await_message == 201:
        timetable_url = await get_group_url(group_id=int(event.object.object.message.text))
        await change_await_message(user_id=user_id, await_value=0)
        logging.debug("Group url received")
        timetable_text = await get_timetable(timetable_url)
        return await event.answer(
            message=timetable_text,
            keyboard=MENU_KB.get_keyboard()
        )
    if await_message == 301:
        university_level = await get_level_id(user_id)
        group_list = await get_university_group_list(from_university_level_id=university_level)
        new_group_id = str(str(university_level) + str(len(group_list)))
        # print(new_group_id)
        group_name, group_url = event.object.object.message.text.split(" ")
        # print(group_url, group_name)
        await add_group(group_id=int(new_group_id), from_university_level_id=university_level, group_url=group_url,
                        group_name=group_name)
        await change_await_message(user_id=user_id, await_value=0)
        return await event.answer(
            message="Создана группа " + str(group_name) + " ей присвоено айди \n " + str(new_group_id) + "рассписание "
                                                                                                      "этой группы "
                                                                                                      "расположено по "
                                                                                                      "ссылки" + str(
                group_url)
        )
