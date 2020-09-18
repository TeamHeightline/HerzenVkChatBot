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
    await_message = IntegerField(default=0)

    class Meta:
        table_name = 'User'


class University(BaseModel):
    university_id = IntegerField(primary_key=True)
    university_name = CharField(max_length=200)


class UniversityLevel(BaseModel):
    from_university = ForeignKeyField(University)
    university_level_name = CharField(max_length=204)
    int_level = IntegerField()
    university_level_id = IntegerField(primary_key=True)


class Group(BaseModel):
    from_university_level = ForeignKeyField(UniversityLevel)
    group_name = CharField(max_length=200)
    group_id = IntegerField(primary_key=True)
    group_url = TextField(default='/static/schedule_view.php?id_group=12459&sem=1')
djalj