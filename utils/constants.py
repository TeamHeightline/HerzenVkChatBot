from vkwave.bots import Keyboard, ButtonColor

MENU_KB = Keyboard()
MENU_KB.add_text_button(text="Расписание", payload={"command": "timetable"}, color=ButtonColor.POSITIVE)
MENU_KB.add_row()
MENU_KB.add_text_button(text="Настройки", payload={"command": "settings"}, color=ButtonColor.SECONDARY)
