from peewee import *

db = MySQLDatabase('csdn', host='127.0.0.1', port=3306, user='dr', password='3253532864')


class BaseModel(Model):
    class Meta:
        database = db

    # def __init__(self, _id, author_name, author_id, title, content, create_at, view_num, comment_num, rating, *args,
    #              **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._id = _id
    #     self.author_name = author_name
    #     self.author_id = author_id
    #     self.title = title
    #     self.content = content
    #     self.create_at = create_at
    #     self.view_num = view_num
    #     self.comment_num = comment_num
    #     self.rating = rating


class Answer(BaseModel):
    post_id = IntegerField()
    author_name = CharField()
    author_id = CharField()
    content = TextField()
    comment_time = DateField()

    like_num = IntegerField()
    comment_num = IntegerField()
    rating = IntegerField()
    status = IntegerField()


class Author(BaseModel):
    user_id = IntegerField(primary_key=True)

    view_num = IntegerField()
    follow_num = IntegerField()
    fans_num = IntegerField()
    original_num = IntegerField()

    rank = IntegerField()
    ip = CharField()
    desc = TextField()
    join_time = DateField()

class Post(BaseModel):

    _id = CharField(primary_key=True)
    # _id = CharField()
    author_name = CharField()
    author_id = CharField()
    title = CharField()
    content = TextField()
    create_at = TimestampField()
    view_num = IntegerField()
    comment_num = IntegerField()
    rating = IntegerField()


if __name__ == '__main__':
    # db.create_tables([Post, Answer, Author])
    # db.create_tables([Post])
    # post1 = Post(
    #     _id='22222',
        # author_name='author_name',
        # author_id='author_id',
        # title='title',
        # content='',
        # create_at=1703174400.0,
        # view_num=1,
        # comment_num=1,
        # rating=1
    # )
    # post1 = Post.create(_id='22222', author_name='author_name', author_id='2', title='1')
    # post1.save()
    pass
