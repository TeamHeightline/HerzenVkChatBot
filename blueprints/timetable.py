from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         CommandsFilter,
                         TextFilter
                         )

from blueprints.services.api import get_timetable
from blueprints.services.dbsystem import get_user_group_id, get_group_url
from utils.constants import MENU_KB

time_table_router = DefaultRouter()


# То, ради чего все затевалось, раааааааааааааааааааааасписание!
@simple_bot_message_handler(time_table_router, PayloadFilter({"command": "timetable"}))
async def time_table_view(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    user_group_id = await get_user_group_id(user_id=user_id)
    time_table_url = await get_group_url(group_id=user_group_id)
    time_table_text = await get_timetable(url=time_table_url)
    if len(time_table_text) < 100:
        time_table_text = "url группы недействителен, ничего не знаю)))"
    return await event.answer(
        message="Расписание : \n" + str(time_table_text)
    )
