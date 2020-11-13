# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class BaseModel(peewee.Model):
    
    class Meta:
        table_name = "basemodel"


@snapshot.append
class University(peewee.Model):
    university_id = IntegerField(primary_key=True)
    university_name = CharField(max_length=200)
    class Meta:
        table_name = "university"


@snapshot.append
class UniversityLevel(peewee.Model):
    university_level_id = IntegerField(primary_key=True)
    from_university = snapshot.ForeignKeyField(index=True, model='university')
    university_level_name = CharField(max_length=204)
    int_level = IntegerField()
    class Meta:
        table_name = "universitylevel"


@snapshot.append
class Group(peewee.Model):
    group_id = IntegerField(primary_key=True)
    from_university_level = snapshot.ForeignKeyField(index=True, model='universitylevel')
    group_name = CharField(max_length=200)
    herzen_group_id = IntegerField()
    subgroup = IntegerField()
    class Meta:
        table_name = "group"


@snapshot.append
class TextTimeTableStorage(peewee.Model):
    timetable_text = TextField()
    herzen_group_id = IntegerField()
    herzen_subgroup = IntegerField()
    class Meta:
        table_name = "texttimetablestorage"


@snapshot.append
class TimeTableStorage(peewee.Model):
    table_url = CharField(max_length=240, unique=True)
    table_file = TextField()
    class Meta:
        table_name = "timetablestorage"


@snapshot.append
class User(peewee.Model):
    user_id = IntegerField(primary_key=True)
    first_name = CharField(max_length=35)
    last_name = CharField(max_length=30)
    is_admin = BooleanField(default=False)
    await_message = IntegerField(default=0)
    group_id = snapshot.ForeignKeyField(index=True, model='group', null=True)
    university_level_id = snapshot.ForeignKeyField(index=True, model='universitylevel', null=True)
    university_id = snapshot.ForeignKeyField(index=True, model='university', null=True)
    class Meta:
        table_name = "User"


