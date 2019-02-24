from peewee import CharField, DateTimeField, Model, SqliteDatabase, TextField

db = SqliteDatabase("my_database.db")


class Post(Model):
    title = CharField(max_length=255)
    slug = CharField(max_length=255, unique=True)
    summary = TextField()
    body = TextField()
    author_name = CharField(max_length=255)
    created_at = DateTimeField()

    class Meta:
        database = db
