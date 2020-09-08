from vkwave.bots import SimpleLongPollBot
import logging
from middlewares import UserEnterMiddleware
from config import TOKEN, GROUP_ID
from blueprints import (test_router,
                        time_table_router
                        )

logging.basicConfig(level="DEBUG")

bot = SimpleLongPollBot(TOKEN, group_id=GROUP_ID)

bot.middleware_manager.add_middleware(UserEnterMiddleware())

bot.dispatcher.add_router(test_router)
bot.dispatcher.add_router(time_table_router)

bot.run_forever()
