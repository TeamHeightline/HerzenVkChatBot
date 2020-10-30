from peewee import *

conn = PostgresqlDatabase("bot_container_db", user="postgres", password="postgres", host="127.0.0.1", port=5432)


# pem add blueprints.services.models.Foo - добаление модели в систему контроля миграций
# pem watch - генерация миграций для всех обноруженных изенений
# pem migrate - отправка миграций в БД


class BaseModel(Model):
    class Meta:
        database = conn


# await_message value:
# 201 - ожидается урл групы

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
    herzen_group_id = IntegerField()
    subgroup = IntegerField()


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    first_name = CharField(max_length=35)
    last_name = CharField(max_length=30)
    is_admin = BooleanField(default=False)
    await_message = IntegerField(default=0)
    group_id = ForeignKeyField(Group, null=True)
    university_level_id = ForeignKeyField(UniversityLevel, null=True)
    university_id = ForeignKeyField(University, null=True)

    class Meta:
        table_name = 'User'


class TimeTableStorage(BaseModel):
    table_url = CharField(max_length=240, unique=True)
    table_file = TextField()


class TextTimeTableStorage(BaseModel):
    timetable_text = TextField()
    herzen_group_id = IntegerField(primary_key=False)
    herzen_subgroup = IntegerField(primary_key=False)


