from vkwave.bots import Keyboard, ButtonColor

MENU_KB = Keyboard()
MENU_KB.add_text_button(text="Расписание", payload={"command": "timetable"}, color=ButtonColor.POSITIVE)
MENU_KB.add_row()
MENU_KB.add_text_button(text="Настройки", payload={"command": "settings"}, color=ButtonColor.SECONDARY)

# Admin keyboard
ADMIN_KB = Keyboard()
ADMIN_KB.add_text_button(text="Добавить группу", payload={"command": "add_group"}, color=ButtonColor.POSITIVE)

TEST_KB = Keyboard(inline=True)
TEST_KB.add_text_button(text="Режим нового пользователя", payload={"command": "начать"}, color=ButtonColor.POSITIVE)
TEST_KB.add_row()
TEST_KB.add_text_button(text="Получение урлов группы", payload={"command": "prepare to get group url"},
                        color=ButtonColor.SECONDARY)

faculties = ['0.0 Волховский филиал',
             "0.1 Выборгский филиал",
             '1.0 Институт информационных технологий и технологического образования',
             '1.1 Институт востоковедения',
             '1.2 Институт детства',
             '1.3 Институт дефектологического образования и реабилитации',
             '1.4 институт иностранных языков',
             '1.5 институт истории и социальных наук',
             '1.6 институт музыки, театра и хореографии',
             '1.7 институт народов Севера',
             '1.8 институт педагогики',
             '1.9 институт психологии',
             '1.10 институт физической культуры и спорта',
             '1.11 институт философии человека',
             '1.12 институт экономики и управления', 'кафедра ЮНЕСКО',
             '2.0 факультет безопасности жизнедеятельности',
             '2.1 факультет биологии',
             '2.2 факультет географии',
             '2.3 факультет изобразительного искусства',
             '2.4 факультет математики',
             '2.5 факультет русского языка как иностранного',
             '2.6 факультет физики',
             '2.7 факультет филологический',
             '2.8 факультет химии',
             '2.9 факультет юридический']


