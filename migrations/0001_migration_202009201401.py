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
    group_url = TextField(default='/static/schedule_view.php?id_group=12459&sem=1')
    subgroup = IntegerField()
    class Meta:
        table_name = "group"


@snapshot.append
class User(peewee.Model):
    user_id = IntegerField(primary_key=True)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    is_admin = BooleanField(default=False)
    await_message = IntegerField(default=0)
    group_id = snapshot.ForeignKeyField(index=True, model='group', null=True)
    university_level_id = snapshot.ForeignKeyField(index=True, model='universitylevel', null=True)
    university_id = snapshot.ForeignKeyField(index=True, model='university', null=True)
    class Meta:
        table_name = "User"


