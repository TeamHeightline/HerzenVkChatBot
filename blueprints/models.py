from peewee import *


conn = PostgresqlDatabase('vk_bot_db', password='2034', user='postgres')

# pem add blueprints.models.Foo - добаление модели в систему контроля миграций
# pem watch - генерация миграций для всех обноруженных изенений
# pem migrate - отправка миграций в БД


class BaseModel(Model):
    class Meta:
        database = conn


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    is_admin = BooleanField(default=False)

    class Meta:
        table_name = 'User'

