from peewee import *
from .models import *


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


async def change_await_message(user_id, await_value):
    u = User.update(await_message=await_value).where(User.user_id == user_id)
    u.save()

