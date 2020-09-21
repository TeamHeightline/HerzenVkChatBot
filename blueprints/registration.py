from vkwave.bots import Keyboard, ButtonColor, SimpleBotEvent, DefaultRouter, simple_bot_message_handler, TextFilter, \
    PayloadFilter

from blueprints.services.dbsistem import change_university

University_KB_1_text = "0 - Волховский филиал \n" \
                       "1 - Выборгский филиал"

University_KB_1 = Keyboard(inline=True)
University_KB_1.add_text_button(text="0", payload={"command": "timetable"}, color=ButtonColor.POSITIVE)
University_KB_1.add_text_button(text="1", payload={"command": "timetable"}, color=ButtonColor.POSITIVE)

University_KB_2_text = "10 - Институт информационных технологий и технологического образования \n" \
                       "11 - Институт востоковедения \n " \
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
        message="Вы выбрали:"
    )
