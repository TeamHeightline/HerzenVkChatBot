from peewee import *
from .models import *

# User.create(user_id=127, first_name='Tim', last_name='Ch')


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


async def get_all_users()->list:
    db_response = User.select().execute()
    user_list = []
    for i in db_response:
        user_list.append(i.user_id)
    return user_list

