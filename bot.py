import threading

from vkwave.bots import SimpleLongPollBot
import logging

from blueprints.scheduler import every_day_subject_sender
from middlewares import UserEnterMiddleware, IsUserAdminMiddleware

from blueprints import (test_router,
                        time_table_router,
                        admin_router,
                        await_router,
                        registration_router
                        )
logging.basicConfig(level="INFO")

TOKEN = "23da22108c2b8eaa19087eff001e14a958599990c22791007b0a52cfeaa7a929c34c98d5f4e639a7195f8"
GROUP_ID = 198502355

bot = SimpleLongPollBot(TOKEN, group_id=GROUP_ID)


t = threading.Thread(target=every_day_subject_sender)
t.start()

bot.middleware_manager.add_middleware(UserEnterMiddleware())


bot.dispatcher.add_router(registration_router)

bot.dispatcher.add_router(test_router)
bot.dispatcher.add_router(time_table_router)

# Warning! ONLY ADMIN PERMISSION

# bot.middleware_manager.add_middleware(IsUserAdminMiddleware())

bot.dispatcher.add_router(admin_router)

# SUPER WARNING!
# Все что ниже этого роутера будет игнорится, в эвэйт роутере регулярка бирет все сообщения, вообще все

bot.dispatcher.add_router(await_router)

bot.run_forever()
