from peewee import *

db = MySQLDatabase('csdn', host='127.0.0.1', port=3306, user='root', password='2280139492')
# 坑！！！
# 主键自定义时，只有使用类名.create()才能写入数据
# 主键非自定义时，直接使用类名()极即可

class Person(Model):
    name = CharField(max_length=20, null=True)
    age = IntegerField(null=True)

    class Meta:
        database = db
        table_name = 'test'


if __name__ == '__main__':
    db.create_tables([Person])

    # 1、将数据保存到数据库中
    xiaohong = Person(name='xiaohong', age=22)
    xiaohong.save()

    xiaohong = Person(name='xiaohong', age=23)
    xiaohong.save()

    sewell = Person(name='sewell', age=24)
    sewell.save()

    xiaoming = Person(name='xiaoming', age=20)
    xiaoming.save()

    # 2、查询数据(两种方式
    # 只会取出第一个符合条件的数据
    # 此种方法取不到数据不会抛出异常
    xiaohong = Person.select().where(Person.name == 'xiaohong').get()
    print(xiaohong.name)
    # 此种方法取不到数据会抛出异常
    xiaohong = Person.get(Person.name == 'xiaohong')
    print(xiaohong.age)
    print('-------')
    # 将全部符合要求的数据返回（不加get方法
    xiaohongs = Person.select().where(Person.name == 'xiaohong')
    for xiaohong in xiaohongs:
        print(xiaohong.name, xiaohong.age)

    # modelselect对象可当做list进行切片等操作
    xiaohongs = Person.select().where(Person.name == 'xiaohong')[1:]
    for xiaohong in xiaohongs:
        print(xiaohong.name, xiaohong.age)

    # 3、改数据
    xiaohongs = Person.select().where(Person.name == 'xiaohong')
    for xiaohong in xiaohongs:
        xiaohong.age += 10
        xiaohong.save()

    # 删除数据
    xiaoming = Person.select().where(Person.name == 'xiaoming').get()
    xiaoming.delete_instance()