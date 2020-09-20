from vkwave.bots import Keyboard, ButtonColor, SimpleBotEvent, DefaultRouter, simple_bot_message_handler, TextFilter

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
                       "15 - институт истории и социальных наук \n" \
                       "16 - институт музыки, театра и хореографии \n " \
                       "17 - институт народов Севера \n " \
                       "18 - институт педагогики \n " \
                       "19 - институт психологии"

University_KB_2 = Keyboard(inline=True)
University_KB_2.add_text_button(text="10", color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="11", color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="12", color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="13", color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="14", color=ButtonColor.POSITIVE)
University_KB_2.add_row()
University_KB_2.add_text_button(text="15", color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="16", color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="17", color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="18", color=ButtonColor.POSITIVE)
University_KB_2.add_text_button(text="19", color=ButtonColor.POSITIVE)


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


registration_router = DefaultRouter()


@simple_bot_message_handler(registration_router, TextFilter(text='начать', ignore_case=True))
async def start_registration(event: SimpleBotEvent):
    await registration_university_1(event=event)
    await registration_university_2(event=event)
    return await event.answer(
        message='Добро пожаловать в бота, пожалуйста, пройдите регистрацию. Для начала выбрите вашу направление',
    )
