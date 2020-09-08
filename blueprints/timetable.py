from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         CommandsFilter,
                         TextFilter
                         )
from utils.constants import MENU_KB

time_table_router = DefaultRouter()


async def create_timetable_text():
    week = [["Информационные технологии \n", "Дискретная математика \n", "Информатика \n"],
            ["Физика \n", "Физика \n"],
            ["Дискретная математика \n"],
            ["Информатика \n", "Информационные технологии в физике \n"],
            ["Информационные технологии в математике \n"],
            ["Физика"]
            ]
    type_text = ''
    for i in range(0, 6):
        for a in (week[i]):
            type_text = type_text + str(a)
        type_text = type_text + "\n"
        print(type_text)


@simple_bot_message_handler(time_table_router, PayloadFilter({"command": "timetable"}))
async def time_table_view(event: SimpleBotEvent):
    return await event.answer(
        message="Расписание" + str(create_timetable_text())
    )
