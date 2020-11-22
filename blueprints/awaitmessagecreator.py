from vkwave.bots import (DefaultRouter,
                         SimpleBotEvent,
                         simple_bot_message_handler,
                         RegexFilter
                         )

from blueprints.services.dbsystem import ActiveUser
import logging
from .registration import new_university, offer_to_register

await_router = DefaultRouter()


#
# 201 - возвращение расписания по урлу
# 301 - создание групы
@simple_bot_message_handler(await_router, RegexFilter(r"."))
async def await_message_processor(event: SimpleBotEvent):
    user_id = event.object.object.message.from_id
    Usr = ActiveUser(id=user_id)
    if Usr.await_message == 301:
        pass
    #     university_level = await get_level_id(user_id)
    #     group_list = await get_university_group_list(from_university_level_id=Usr.university_level_id)
    #     new_group_id = str(str(university_level) + str(len(group_list)))
    #     group_name, group_url = event.object.object.message.text.split(" ")
    #     await add_group(group_id=int(new_group_id), from_university_level_id=Usr.university_level_id, group_url=group_url,
    #                     group_name=group_name)
    #     await change_await_message(user_id=user_id, await_value=0)
    #     return await event.answer(
    #         message="Создана группа " + str(group_name) + " ей присвоено айди \n " + str(new_group_id) +
    #                 "рассписание этой группы расположено по ссылки" + str(group_url)
    #     )
    else:
        user_id = event.object.object.message.from_id
        Usr = ActiveUser(user_id)
        if not hasattr(Usr, "first_name") or Usr.university_id is None:
            await offer_to_register(event=event, user_id=user_id)
        else:
            logging.info(Usr.first_name + " " + Usr.last_name + " написал " + event.object.object.message.text)

