import datetime

from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         CommandsFilter,
                         TextFilter
                         )

from blueprints.services.api import get_timetable, new_get_timetable, new_get_timetable_for_week_day
from blueprints.services.dbsystem import get_user_group_id, get_herzen_group_id, get_herzen_subgroup
from utils.constants import MENU_KB

time_table_router = DefaultRouter()


# То, ради чего все затевалось, раааааааааааааааааааааасписание!
@simple_bot_message_handler(time_table_router, PayloadFilter({"command": "timetable"}))
async def time_table_view(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    user_group_id = await get_user_group_id(user_id=user_id)
    time_table_herzen_group_id = await get_herzen_group_id(group_id=user_group_id)
    time_table_herzen_subgroup = await get_herzen_subgroup(group_id=user_group_id)
    time_table_text = await new_get_timetable(groupID=time_table_herzen_group_id, subgroup=time_table_herzen_subgroup)
    if len(time_table_text) < 100:
        time_table_text = "ошибка в данных группы, неверно указан groupID или subgroup"
    return await event.answer(
        message="Расписание : \n" + str(time_table_text)
    )


@simple_bot_message_handler(time_table_router, PayloadFilter({"command": "today_timetable"}))
async def time_table_view(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    user_group_id = await get_user_group_id(user_id=user_id)
    time_table_herzen_group_id = await get_herzen_group_id(group_id=user_group_id)
    time_table_herzen_subgroup = await get_herzen_subgroup(group_id=user_group_id)
    time_table_text = await new_get_timetable_for_week_day(groupID=time_table_herzen_group_id,
                                                           subgroup=time_table_herzen_subgroup,
                                                           day=datetime.datetime.weekday(datetime.datetime.now()))
    if len(time_table_text) < 100:
        time_table_text = "ошибка в данных группы, неверно указан groupID или subgroup"
    return await event.answer(
        message="Расписание : \n" + str(time_table_text)
    )


@simple_bot_message_handler(time_table_router, PayloadFilter({"command": "next_day_timetable"}))
async def time_table_view(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    user_group_id = await get_user_group_id(user_id=user_id)
    time_table_herzen_group_id = await get_herzen_group_id(group_id=user_group_id)
    time_table_herzen_subgroup = await get_herzen_subgroup(group_id=user_group_id)
    time_table_text = await new_get_timetable_for_week_day(groupID=time_table_herzen_group_id,
                                                           subgroup=time_table_herzen_subgroup,
                                                           day=(datetime.datetime.weekday(datetime.datetime.now()) + 1))
    if len(time_table_text) < 100:
        time_table_text = "ошибка в данных группы, неверно указан groupID или subgroup"
    return await event.answer(
        message="Расписание : \n" + str(time_table_text)
    )


@simple_bot_message_handler(time_table_router, PayloadFilter({"command": "previous_day_timetable"}))
async def time_table_view(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    user_group_id = await get_user_group_id(user_id=user_id)
    time_table_herzen_group_id = await get_herzen_group_id(group_id=user_group_id)
    time_table_herzen_subgroup = await get_herzen_subgroup(group_id=user_group_id)
    time_table_text = await new_get_timetable_for_week_day(groupID=time_table_herzen_group_id,
                                                           subgroup=time_table_herzen_subgroup,
                                                           day=(datetime.datetime.weekday(datetime.datetime.now()) - 1))
    if len(time_table_text) < 10:
        time_table_text = "ошибка в данных группы, неверно указан groupID или subgroup"
    return await event.answer(
        message="Расписание : \n" + str(time_table_text)
    )