from peewee import *

database = MySQLDatabase('make_name',
                         **{'user': 'root', 'charset': 'utf8', 'use_unicode': True, 'host': '119.27.187.220',
                            'port': 3306, 'password': 'Zongwen123!@#'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Poems(BaseModel):
    author = CharField()
    author_id = IntegerField()
    content = TextField()
    dynasty = CharField(null=True)
    title = CharField()

    class Meta:
        table_name = 'poems'


class PoemsAuthor(BaseModel):
    dynasty = CharField(null=True)
    intro_l = TextField(null=True)
    intro_s = TextField()
    name = CharField()

    class Meta:
        table_name = 'poems_author'


class Poetry(BaseModel):
    author = CharField()
    author_id = IntegerField()
    content = TextField()
    dynasty = CharField()
    title = CharField()
    yunlv_rule = TextField()

    class Meta:
        table_name = 'poetry'


class PoetryAuthor(BaseModel):
    dynasty = CharField(null=True)
    intro = TextField(null=True)
    name = CharField()

    class Meta:
        table_name = 'poetry_author'
