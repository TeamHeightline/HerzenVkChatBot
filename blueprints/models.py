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

