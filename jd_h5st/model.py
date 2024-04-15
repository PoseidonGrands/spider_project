from peewee import *
import pymysql

db = MySQLDatabase('jd', host='127.0.0.1', port=3306, user='root', password='2280139492')


class BaseModel(Model):
    class Meta:
        database = db


class Good(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=300)
    price = IntegerField()
    business = CharField(50, verbose_name='店铺名称')
    express = CharField(20, verbose_name='快递名称')
    ggbz = TextField(default='', verbose_name='规格和包装')
    has_good = CharField(10, verbose_name='是否有货')
    img_list = TextField(default='', verbose_name='商品展示图列表')

    good_comment_scale = IntegerField(default=0, verbose_name='好评率')
    comments_num = IntegerField(verbose_name='评论数')
    has_pic_comments = IntegerField(default=0, verbose_name='有图评论')
    has_video_comments = IntegerField(default=0, verbose_name='有视频的评论')
    append_comments = IntegerField(default=0, verbose_name='追加评价')
    good_comments = IntegerField(default=0, verbose_name='好评率')
    middle_comments = IntegerField(default=0, verbose_name='中评率')
    bad_comments = IntegerField(default=0, verbose_name='差评数')


class GoodEvaluate(BaseModel):
    id = IntegerField(primary_key=True)
    good = ForeignKeyField(Good)
    user_name = CharField()
    good_info = TextField()
    content = TextField()
    evaluate_time = DateField()
    star = IntegerField(verbose_name='评分')
    like_num = IntegerField(verbose_name='点赞数')
    comment_num = IntegerField(verbose_name='评价数')
    pic_list = TextField()
    video_list = TextField()


class GoodCommentTag(BaseModel):
    id = IntegerField(primary_key=True)
    tag = CharField(20)
    num = IntegerField()


if __name__ == '__main__':
    db.create_tables([Good, GoodEvaluate, GoodCommentTag])
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
    # 两种方式
    # post1 = Post.create(_id='22222', author_name='author_name', author_id='2', title='1')
    # post1.save()
    pass
