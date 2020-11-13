from blueprints.services.models import *
import logging


async def create_user(user_id, first_name, last_name):
    User.create(user_id=user_id, first_name=first_name, last_name=last_name)


class ActiveUser(object):
    def __init__(self, id:int):
        self.id = id
        db_response = User.select().where(User.user_id == self.id).execute()
        for i in db_response:
            try:
                self.first_name = i.first_name
                self.last_name = i.last_name
                self.group_id = i.group_id
                self.group_id = i.group_id
                self.university_level_id = i.university_level_id
                self.await_message = i.await_message
                self.is_admin = i.is_admin
                self.herzen_group_id = i.herzen_group_id
                self.university_id = i.university_id
            except:
                pass

    async def change_user_group_id(self):
        User.update(group_id=self.group_id).where(User.user_id == self.id).execute()
        logging.debug("group id level changed")

    async def change_await_message(self):
        User.update(await_message=self.await_message).where(User.user_id == self.id).execute()
        logging.debug("await message changed")

    async def change_university(self):
        User.update(university_id=self.university_id).where(User.user_id == self.id).execute()
        logging.debug("university changed")

    async def change_university_level(self):
        User.update(university_level_id=self.university_level_id).where(User.user_id == self.id).execute()
        logging.debug("university level changed")

    @staticmethod
    async def get_all_users() -> list:
        db_response = User.select().execute()
        user_list = []
        for i in db_response:
            user_list.append(i.user_id)
        return user_list


class ActiveGroup(object):
    def __init__(self, group_id):
        self.id = group_id
        db_response = Group.select().where(Group.group_id == self.id).execute()
        for i in db_response:
            try:
                self.herzen_group_id = i.herzen_group_id
                self.subgroup = i.subgroup
            except:
                pass

    @staticmethod
    async def add_group(group_name: str, group_id: int, from_university_level_id: int, group_url: str,
                        subgroup: int = 0):
        Group.create(group_id=group_id, group_name=group_name, from_university_level_id=from_university_level_id,
                     group_url=group_url,
                     subgroup=subgroup)

    @staticmethod
    async def get_university_group_list(from_university_level_id: int) -> list:
        db_response = Group.select().where(Group.from_university_level == from_university_level_id)
        group_list = [[]]
        for i in db_response:
            try:
                group_list.append([i.group_name, i.group_id])
            except:
                pass
        return group_list


async def get_university_group_list(from_university_level_id: int) -> list:
    db_response = Group.select().where(Group.from_university_level == from_university_level_id)
    group_list = [[]]
    for i in db_response:
        try:
            group_list.append([i.group_name, i.group_id])
        except:
            pass
    return group_list





