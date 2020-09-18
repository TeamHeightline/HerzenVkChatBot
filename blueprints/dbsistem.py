from peewee import *
from .models import *
import logging


async def create_user(user_id, first_name, last_name):
    User.create(user_id=user_id, first_name=first_name, last_name=last_name)


async def get_user(user_id):
    db_response = User.select().where(User.user_id == user_id).execute()
    first_name = None
    last_name = None
    for i in db_response:
        try:
            first_name = i.first_name
            last_name = i.last_name
        except:
            return None, None
    else:
        return first_name, last_name


async def get_all_users() -> list:
    db_response = User.select().execute()
    user_list = []
    for i in db_response:
        user_list.append(i.user_id)
    return user_list


async def is_user_admin(user_id):
    db_response = User.select().where(User.user_id == user_id).execute()
    for i in db_response:
        try:
            is_admin = i.is_admin
        except:
            return None
    return is_admin


async def gey_await_message(user_id:int)->int:
    db_response = User.select().where(User.user_id == user_id).execute()
    for i in db_response:
        try:
            await_message = i.await_message
        except:
            return 0
    logging.debug("Await message successfully received")
    return await_message


async def change_await_message(user_id, await_value):
    u = User.update(await_message=await_value).where(User.user_id == user_id).execute()
    logging.debug("await message changed")


async def get_group_url(group_id):
    db_response = Group.select().where(Group.group_id == group_id).execute()
    for i in db_response:
        try:
            group_url = i.group_url
        except:
            return None
    logging.debug("Group URL successfully received")
    return group_url

