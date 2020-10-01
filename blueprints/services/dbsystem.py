from blueprints.services.models import *
import logging
import ast
import re


async def create_user(user_id, first_name, last_name):
    User.create(user_id=user_id, first_name=first_name, last_name=last_name)


async def get_user(user_id: int):
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


async def get_user_group_id(user_id: int):
    db_response = User.select().where(User.user_id == user_id).execute()
    for i in db_response:
        try:
            group_id = i.group_id
        except:
            return None
    return group_id


async def get_all_users() -> list:
    db_response = User.select().execute()
    user_list = []
    for i in db_response:
        user_list.append(i.user_id)
    return user_list


async def is_user_admin(user_id: int):
    db_response = User.select().where(User.user_id == user_id).execute()
    for i in db_response:
        try:
            is_admin = i.is_admin
        except:
            return None
    return is_admin


async def gey_await_message(user_id: int) -> int:
    db_response = User.select().where(User.user_id == user_id).execute()
    for i in db_response:
        try:
            await_message = i.await_message
        except:
            return 0
    logging.debug("Await message successfully received")
    return await_message


async def change_await_message(user_id: int, await_value: int):
    u = User.update(await_message=await_value).where(User.user_id == user_id).execute()
    logging.debug("await message changed")


async def get_group_url(group_id: int):
    db_response = Group.select().where(Group.group_id == group_id).execute()
    for i in db_response:
        try:
            group_url = i.group_url
        except:
            return None
    logging.debug("Group URL successfully received")
    return group_url


async def change_university(user_id: int, university_id: int):
    u = User.update(university_id=university_id).where(User.user_id == user_id).execute()
    logging.debug("university changed")


async def gey_university_id(user_id: int) -> int:
    db_response = User.select().where(User.user_id == user_id).execute()
    for i in db_response:
        try:
            university_id = i.university_id
        except:
            return 0
    logging.debug("Await message successfully received")
    return university_id


async def change_university_level(user_id: int, university_level_id: int):
    u = User.update(university_level_id=university_level_id).where(User.user_id == user_id).execute()
    logging.debug("university level changed")


async def get_level_id(user_id: int) -> int:
    db_response = User.select().where(User.user_id == user_id).execute()
    for i in db_response:
        try:
            university_level_id = i.university_level_id
        except:
            return 0
    logging.debug("University level successfully received")
    return university_level_id


async def get_university_group_list(from_university_level_id: int) -> list:
    db_response = Group.select().where(Group.from_university_level == from_university_level_id)
    group_list = [[]]
    for i in db_response:
        try:
            group_list.append([i.group_name, i.group_id])
        except:
            pass
    return group_list


async def change_user_group_id(user_id: int, group_id: int):
    u = User.update(group_id=group_id).where(User.user_id == user_id).execute()
    logging.debug("group id level changed")


async def add_group(group_name: str, group_id: int, from_university_level_id: int, group_url: str,
                    subgroup: int = 0) -> int:
    Group.create(group_id=group_id, group_name=group_name, from_university_level_id=from_university_level_id,
                 group_url=group_url,
                 subgroup=subgroup)
    return 1


async def add_time_table_file(table_url: str, table_file: str):
    TimeTableStorage.create(table_url=table_url, table_file=table_file)


async def get_time_table_file(table_url: str):
    db_response = TimeTableStorage.select().where(TimeTableStorage.table_url == table_url).execute()
    table_file = ''
    for i in db_response:
        try:
            table_file = i.table_file
        except:
            return 0
    logging.debug("Table file successfully received")
    return table_file


async def get_group_time_table_file(group_id: int) -> dict:
    group_url = await get_group_url(group_id=group_id)
    file = str(await get_time_table_file(table_url=group_url))
    file = re.sub("^\s+|\n|\r|\s+$", '', file)
    print (ast.literal_eval(file))
    return ast.literal_eval(file)


