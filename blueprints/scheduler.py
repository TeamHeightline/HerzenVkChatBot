import asyncio
import datetime
import time

import vk_bot
import schedule

from blueprints.services.api import get_subject
from blueprints.services.dbsystem import ActiveUser, ActiveGroup

bot = vk_bot.VkBot('23da22108c2b8eaa19087eff001e14a958599990c22791007b0a52cfeaa7a929c34c98d5f4e639a7195f8')


class User(object):
    def __init__(self, id):
        self.id = id


def send_msg(text, user_id):
    u = User(id=user_id)

    bot.vk.Message.send(
        peer=u,
        message=text
    )


def send_to_all_user(nomber_of_subject):
    user_list = ActiveUser.get_all_users()
    print(user_list)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for i in user_list:
        usr = ActiveUser(id=int(i))
        agr = ActiveGroup(group_id=usr.group_id)
        text = loop.run_until_complete(
            get_subject(groupID=agr.herzen_group_id, subgroup=agr.subgroup, day=datetime.datetime.weekday(datetime
                                                                                                          .datetime.now()),
                        number_of_subject=nomber_of_subject))
        send_msg(user_id=i, text=text)


# Время отличается на 3 часа, т.к. датацентр в другом часовом поясе
def every_day_subject_sender():
    schedule.every().day.at("04:50").do(send_to_all_user, 0)
    schedule.every().day.at("06:35").do(send_to_all_user, 1)
    schedule.every().day.at("08:20").do(send_to_all_user, 2)
    schedule.every().day.at("10:20").do(send_to_all_user, 3)
    while True:
        schedule.run_pending()
        time.sleep(1)
