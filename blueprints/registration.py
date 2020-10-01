from vkwave.bots import Keyboard, ButtonColor, SimpleBotEvent, DefaultRouter, simple_bot_message_handler, TextFilter, \
    PayloadFilter

from blueprints.services.dbsystem import change_university, gey_university_id, change_university_level, get_level_id, \
    get_university_group_list, change_user_group_id

# Доки ) короче, документация, здесь у нас модуль регистрации, вот так вот, вообще, что туть происходит,
# здесь у нас хрянятся клавиатуды со всеми университетами, значениям на кнопушках соответствует ячейка
# university_id в базе. Когда юзер впервые заходит и пишет "начать", срабатывает метод start_registration
# он подтягивает 4 метода для выбора университета, каждый метод - стек по 10 университетов
# когда юзер выбирает университет с клавиатуры, срабатывает payload - set university, по этому пэйлоду
# срабатывает метод set_university, значение университета записывается в базу, после этого  пользователю
# отправляют сообщение с прозьбой выбора курса и кнопками, по нажатию кнопок срабатывает payload - set level
# дальше вообще магия, этот пэйлод поднимает метод set_group, он собирает вместе айди уника и курса,
# получается university_level_id он и идет в базу данных
from utils.constants import MENU_KB

University_KB_1_text = "0 - Волховский филиал \n" \
                       "1 - Выборгский филиал"

University_KB_1 = Keyboard(inline=True)
University_KB_1.add_text_button(text="0", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_1.add_text_button(text="1", payload={"command": "set university"}, color=ButtonColor.POSITIVE)

University_KB_2_text = "10 - Институт информационных технологий и технологического образования \n" \
                       "11/зжх*-89 - Институт востоковедения \n " \
                       "12 - Институт детства \n " \
                       "13 - Институт дефектологического образования и реабилитации \n " \
                       "14 - Институт иностранных языков \n " \
                       "15 - Институт истории и социальных наук \n" \
                       "16 - Институт музыки, театра и хореографии \n " \
                       "17 - Институт народов Севера \n " \
                       "18 - Институт педагогики \n " \
                       "19 - Институт психологии"

University_KB_2 = Keyboard(inline=True)
University_KB_2.add_text_button(text="10", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="11", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="12", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="13", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="14", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_2.add_row()
University_KB_2.add_text_button(text="15", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="16", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="17", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="18", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="19", payload={"command": "set university"}, color=ButtonColor.POSITIVE)

University_KB_3_text = "20 - Факультет безопасности жизнедеятельности\n" \
                       "21 - Факультет биологии\n" \
                       "22 - Факультет географии\n" \
                       "23 - Факультет изобразительного искусства\n" \
                       "24 - Факультет математики\n" \
                       "25 - Факультет русского языка как иностранного\n" \
                       "26 - Факультет физики\n" \
                       "27 - Факультет филологический\n" \
                       "28 - Факультет химии\n" \
                       "29 - Факультет юридический\n"

University_KB_3 = Keyboard(inline=True)
University_KB_3.add_text_button(text="20", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_3.add_text_button(text="21", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_3.add_text_button(text="22", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_3.add_text_button(text="23", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_3.add_text_button(text="24", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_3.add_row()
University_KB_3.add_text_button(text="25", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_3.add_text_button(text="26", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_3.add_text_button(text="27", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_3.add_text_button(text="28", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_3.add_text_button(text="29", payload={"command": "set university"}, color=ButtonColor.POSITIVE)

University_KB_4_text = "110 - Институт физической культуры и спорта" \
                       "111 - Институт философии человека" \
                       "112 - Институт экономики и управления" \
                       "113 - Кафедра ЮНЕСКО"
University_KB_4 = Keyboard(inline=True)

University_KB_4.add_text_button(text="110", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_4.add_text_button(text="111", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_4.add_text_button(text="112", payload={"command": "set university"}, color=ButtonColor.POSITIVE)
University_KB_4.add_text_button(text="113", payload={"command": "set university"}, color=ButtonColor.POSITIVE)

University_Level_KB = Keyboard(inline=True)
University_Level_KB.add_text_button(text="1", payload={"command": "set level"}, color=ButtonColor.POSITIVE)
University_Level_KB.add_text_button(text="2", payload={"command": "set level"}, color=ButtonColor.POSITIVE)
University_Level_KB.add_text_button(text="3", payload={"command": "set level"}, color=ButtonColor.POSITIVE)
University_Level_KB.add_text_button(text="4", payload={"command": "set level"}, color=ButtonColor.POSITIVE)


async def registration_university_1(event: SimpleBotEvent):
    return await event.answer(
        message=University_KB_1_text,
        keyboard=University_KB_1.get_keyboard()
    )


async def registration_university_2(event: SimpleBotEvent):
    return await event.answer(
        message=University_KB_2_text,
        keyboard=University_KB_2.get_keyboard()
    )


async def registration_university_3(event: SimpleBotEvent):
    return await event.answer(
        message=University_KB_3_text,
        keyboard=University_KB_3.get_keyboard()
    )


async def registration_university_4(event: SimpleBotEvent):
    return await event.answer(
        message=University_KB_4_text,
        keyboard=University_KB_4.get_keyboard()
    )


registration_router = DefaultRouter()


@simple_bot_message_handler(registration_router, TextFilter(text='начать', ignore_case=True))
async def start_registration(event: SimpleBotEvent):
    await registration_university_1(event=event)
    await registration_university_2(event=event)
    await registration_university_3(event=event)
    await registration_university_4(event=event)
    return await event.answer(
        message='Добро пожаловать в бота, пожалуйста, пройдите регистрацию. Для начала выбрите ваше направление',
    )


@simple_bot_message_handler(registration_router, PayloadFilter({"command": "set university"}))
async def set_university(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    university_id = int(event.object.object.message.text)
    await change_university(user_id=user_id, university_id=university_id)
    return await event.answer(
        message="Теперь выбирети ваш курс",
        keyboard=University_Level_KB.get_keyboard()
    )


async def group_to_message(group_list: list) -> (object, str):
    GROUP_KB = Keyboard(inline=True)
    group_text = ''
    for i in range(len(group_list)):
        try:
            group_text += str(group_list[i][1]) + " - " + str(group_list[i][0] + "\n")
            GROUP_KB.add_text_button(text=group_list[i][1], payload={"command": "set group"},
                                     color=ButtonColor.POSITIVE)
        except:
            pass
        if (i % 5 == 0) and (i != 0):
            GROUP_KB.add_row()
    return GROUP_KB, group_text


@simple_bot_message_handler(registration_router, PayloadFilter({"command": "set level"}))
async def set_level(event: SimpleBotEvent):
    # отвечает за то, чтобы записать челокеку его university_level_id
    user_id = event.object.object.message.from_id
    text = event.object.object.message.text
    university_id = await gey_university_id(user_id=user_id)
    university_level_id = int(str(university_id) + str(text))
    await change_university_level(user_id=user_id, university_level_id=university_level_id)
    # на основе уровня Направление -> Курс, добывает из базы список групп для этого курса
    university_level = await get_level_id(user_id=user_id)
    group_list = await get_university_group_list(from_university_level_id=university_level)
    # Превращение списка групп в конечное сообщение с клавиатурой
    GROUP_KB, group_text = await group_to_message(group_list=group_list)
    return await event.answer(
        message=("Теперь выбирети вашу группу \n " + group_text),
        keyboard=GROUP_KB.get_keyboard()
    )


@simple_bot_message_handler(registration_router, PayloadFilter({"command": "set group"}))
async def set_group(event: SimpleBotEvent):
    user_id = int(event.object.object.message.from_id)
    group_id = int(event.object.object.message.text)
    await change_user_group_id(user_id=user_id, group_id=group_id)
    return await event.answer(
        message="Регистрация окончена, теперь вам доступно ваше расписание",
        keyboard=MENU_KB.get_keyboard()

    )
