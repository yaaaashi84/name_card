from playhouse.db_url import connect
from peewee import Model
from peewee import IntegerField
from peewee import CharField
from flask_login import UserMixin

db = connect("sqlite:///peewee_db.sqlite")

if not db.connect():
    print("接続NG")
    exit()
print("接続OK")

class User(UserMixin, Model):
    id = IntegerField(primary_key=True)  # 数字
    create_id = CharField(unique=True)
    name = CharField()  # 文字
    password = CharField()  # 文字
    belong = CharField()
    position = CharField()
    tel = CharField()
    email = CharField()
    comment = CharField()
    link = CharField()
    icon = CharField(null=True)

    class Meta:  # 内部クラス
        database = db
        table_name = "user"

class Friend(Model):
    create_id_from = CharField()
    create_id_to = CharField()

    class Meta:  # 内部クラス
        database = db
        table_name = "friend"


# db.drop_tables([User])
db.create_tables([User])
db.create_tables([Friend])