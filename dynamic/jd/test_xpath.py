from scrapy import Selector


with open('resources/source.html', 'r') as f:
    html_content = f.read()

sel = Selector(text=html_content)
name = ''.join(sel.xpath('//div[@class="sku-name"]/text()').extract()).strip()
print(name)
price = sel.xpath('//span[@class="p-price"]/span').extract()
print(price)
# business = CharField(50, verbose_name='店铺名称')
# express = CharField(20, verbose_name='快递名称')
# ggbz = TextField(default='', verbose_name='规格和包装')
# has_good = CharField(10, verbose_name='是否有货')
# img_list = TextField(default='', verbose_name='商品展示图列表')
#
# good_comment_scale = IntegerField(default=0, verbose_name='好评率')
# comments_num = IntegerField(verbose_name='评论数')
# has_pic_comments = IntegerField(default=0, verbose_name='有图评论')
# has_video_comments = IntegerField(default=0, verbose_name='有视频的评论')
# append_comments = IntegerField(default=0, verbose_name='追加评价')
# good_comments = IntegerField(default=0, verbose_name='好评率')
# middle_comments = IntegerField(default=0, verbose_name='中评率')
# bad_comments = IntegerField(default=0, verbose_name='差评数')