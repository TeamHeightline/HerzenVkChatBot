import datetime

from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         CommandsFilter,
                         TextFilter
                         )

from blueprints.services.api import new_get_timetable, new_get_timetable_for_week_day
from blueprints.services.dbsystem import ActiveUser, ActiveGroup
from utils.constants import MENU_KB

time_table_router = DefaultRouter()


# То, ради чего все затевалось, раааааааааааааааааааааасписание!
@simple_bot_message_handler(time_table_router, PayloadFilter({"command": "timetable"}))
async def time_table_view(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    Usr = ActiveUser(id=user_id)
    herzenGroup = ActiveGroup(group_id=Usr.group_id)
    time_table_text = await new_get_timetable(groupID=herzenGroup.herzen_group_id, subgroup=herzenGroup.subgroup)
    if len(time_table_text) < 5:
        time_table_text = "ошибка в данных группы, неверно указан groupID или subgroup"
    return await event.answer(
        message="Расписание : \n" + str(time_table_text)
    )


@simple_bot_message_handler(time_table_router, PayloadFilter({"command": "today_timetable"}))
async def time_table_view(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    Usr = ActiveUser(id=user_id)
    herzenGroup = ActiveGroup(group_id=Usr.group_id)
    time_table_text = await new_get_timetable_for_week_day(groupID=herzenGroup.herzen_group_id,
                                                           subgroup=herzenGroup.subgroup,
                                                           day=datetime.datetime.weekday(datetime.datetime.now()))
    if len(time_table_text) < 5:
        time_table_text = "ошибка в данных группы, неверно указан groupID или subgroup"
    return await event.answer(
        message="Расписание : \n" + str(time_table_text)
    )


@simple_bot_message_handler(time_table_router, PayloadFilter({"command": "next_day_timetable"}))
async def time_table_view(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    Usr = ActiveUser(id=user_id)
    herzenGroup = ActiveGroup(group_id=Usr.group_id)
    time_table_text = await new_get_timetable_for_week_day(groupID=herzenGroup.herzen_group_id,
                                                           subgroup=herzenGroup.subgroup,
                                                           day=(datetime.datetime.weekday(datetime.datetime.now()) + 1))
    if len(time_table_text) < 5:
        time_table_text = "ошибка в данных группы, неверно указан groupID или subgroup"
    return await event.answer(
        message="Расписание : \n" + str(time_table_text)
    )


@simple_bot_message_handler(time_table_router, PayloadFilter({"command": "previous_day_timetable"}))
async def time_table_view(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    Usr = ActiveUser(id=user_id)
    herzenGroup = ActiveGroup(group_id=Usr.group_id)
    time_table_text = await new_get_timetable_for_week_day(groupID=herzenGroup.herzen_group_id,
                                                           subgroup=herzenGroup.subgroup,
                                                           day=(datetime.datetime.weekday(datetime.datetime.now()) - 1))
    if len(time_table_text) < 5:
        time_table_text = "ошибка в данных группы, неверно указан groupID или subgroup"
    return await event.answer(
        message="Расписание : \n" + str(time_table_text)
    )