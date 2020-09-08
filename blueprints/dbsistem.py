from peewee import *

conn = PostgresqlDatabase('vk_bot_db', password='2034', user='postgres')


class BaseModel(Model):
    class Meta:
        database = conn


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)

    class Meta:
        table_name = 'User'


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


print(get_user(127))
