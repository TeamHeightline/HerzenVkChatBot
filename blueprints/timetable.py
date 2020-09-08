from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         PayloadFilter,
                         CommandsFilter,
                         TextFilter
                         )
from utils.constants import MENU_KB

time_table_router = DefaultRouter()


def create_timetable_text() -> str:
    week = [["Информационные технологии [лаб] \n", "Дискретная математика [практ]\n", "Информатика [лекц]\n"],
            ["Физика [лекц]\n", "Физика [лекц]\n"],
            ["Дискретная математика [практ]\n"],
            ["Информатика [лаб]\n", "Информационные технологии в физике [лаб]\n"],
            ["Информационные технологии в математике [лаб]\n", "Физика [лаб]\n", "Основы компьютерной алгебры [""лаб]\n",
             "Физическая культура и спорт [практ]\n"],
            ["Иностранный язык[лекц]\n"], ["Физическая культура[лекц] \n"], ["Философия[лекц] \n"]
            ]
    type_text = ''
    for i in range(0, 6):
        for a in (week[i]):
            type_text = type_text + str(a)
        type_text = type_text + "\n"
    return type_text


@simple_bot_message_handler(time_table_router, PayloadFilter({"command": "timetable"}))
async def time_table_view(event: SimpleBotEvent):
    return await event.answer(
        message="Расписание : \n" + str(create_timetable_text())
    )
