import requests
import os
import re
import time
from fake_useragent import UserAgent

from scrapy import Selector
from datetime import datetime
from models import Post


urls_set = set()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Cookie': 'uuid_tt_dd=10_18853603210-1680152514986-783151; c_adb=1; pixelhecomment_new=1705462247593; cf_clearance=RhFHerugKfVmPrBmvsKaTNDOB_g.vX0gEQK17i2Db98-1711906562-1.0.1.1-ky7Vza7yV2TrRLJzbO9sEGD.2RaoUOgHruUt2lRCC3r3PnRUCRFMiyDN_ZDqD1mRth3Oyu.x_VDadsTfcCP1kA; historyList-new=%5B%5D; c_dl_prid=1711906680308_471825; c_dl_rid=1711906722489_471355; c_dl_fref=https://so.csdn.net/so/search; c_dl_fpage=/download/zzjlhlcd/85656672; c_dl_um=distribute.pc_relevant_download.none-task-download-2%7Edefault%7ELANDING_RERANK%7ERate-1-19408265-download-10962106.257%5Ev14%5Epc_dl_relevant_base1_a; loginbox_strategy=%7B%22taskId%22%3A317%2C%22abCheckTime%22%3A1711945147481%2C%22version%22%3A%22ExpA%22%2C%22nickName%22%3A%22pixelhe%22%2C%22blog-threeH-dialog-expa%22%3A1711905732186%7D; UserName=2401_83556130; UserInfo=24c309fa5b2d4a22a424fb9c894fab63; UserToken=24c309fa5b2d4a22a424fb9c894fab63; UserNick=%E5%AD%A6%E9%9C%B8%E9%A3%9E%E9%A3%9E5; AU=06D; UN=2401_83556130; BT=1711945188278; p_uid=U110000; dp_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTExMDg3NiwiZXhwIjoxNzEyNTQ5OTk1LCJpYXQiOjE3MTE5NDUxOTUsInVzZXJuYW1lIjoiMjQwMV84MzU1NjEzMCJ9._VasKBw7nH61JNX_mf7dAOaYrgvjSQ6DcUuFdGztgs0; ssxmod_itna=iqGhY5BK0IxmorDz=D2YLE8ZDfgHxQTRvmuDKDsa1bDSxGKidDqxBmmlDDtTtetSi7H+W4qhOihW5Qj8iAxEFjLTfGTpn4iTD4q07Db4GkDAqiOD7TRtoD4RKGwD0eG+DD4DWCqDt/ENqDFUqtS0kLu3LLnUqDEtkQDYMQDmLbDnhiVDlU6f7iDf8QDIwXu/4GnD0QWNdRMD0f35PaDzkQDbopBf6FDtwTR/4DHnLXVtqHo4hGW7F4s8u3rf7vq3YmK0A8PCAvLyIhPASGiiS+oi5DACDEnPD===; ssxmod_itna2=iqGhY5BK0IxmorDz=D2YLE8ZDfgHxQTRvmuDikAaYqDl=jCDj42QM2LuZUTvL6=yFDCIw1OCxAp3ybBCg4wnbfm3a+QsSi8c3Yq=CEAk1GRnKDCUpzCTmV7FMQbA94bAb2G2kfeO4wOushgpsh7FPOg0GqjFYXlyGiz9Du0ebOPKTLpx3DQKxUD08DYKx4D=; dc_sid=f9375c46a6486d16edea87215563552b; c_segment=15; csrfToken=7zhI99Hgq8NSiG88JnMljkHb; dc_session_id=10_1712189938555.454105; fe_request_id=1712190018732_6569_6627891; 2401_83556130comment_new=1711709421083; firstDie=1; c_pref=default; c_first_ref=default; c_ref=default; c_first_page=https%3A//bbs.csdn.net/forums/edu; c_dsid=11_1712195769723.301181; c_page_id=default; log_Id_pv=728; log_Id_view=17442; log_Id_click=553; dc_tos=sbeax9'
}


# 把地址都提取出来
def get_urls():
    base_path = os.path.join(os.getcwd(), 'url_nav_recommend.txt')
    with open(base_path, 'r') as f:
        line = f.readline()
        _re = re.compile(r'"(.*)"')
        while line:
            urls_set.add(_re.search(line).group(1))
            # 继续读取
            line = f.readline()


# def spider_page_by_json(url, _headers):
#     """方法二：分析网站，直接提取json
#         暂时未能实现，又是需要js逆向反爬
#     """
#     # 爬取社区默认页，从html提取出communityId，通过此值请求json数据
#     res = requests.get('https://bbs.csdn.net/forums/edu', headers=_headers)
#     if res.status_code == 200:
#         community_id = re.search(r'"community":.*communityId":\s*(.*)?,"bgImage"', res.text).group(1)
#         # 拼接请求参数
#         params = {
#             'page': 1,
#             'pageSize': 20,
#             'noMore': False,
#             'type': 1,
#             'communityId': 3661
#         }
#         resp = requests.get('https://bizapi.csdn.net/community-cloud/v1/community/listV2', headers=_headers, params=params)
#         print(resp.text)
#             # try:
#             #     post = Post.create(
#             #         _id=content_id,
#             #         author_name=author_name,
#             #         author_id=author_id,
#             #         title=title,
#             #         pcontent='',
#             #         create_at=create_at,
#             #         view_num=view_num,
#             #         comment_num=comment_num,
#             #         rating=rating
#             #     )
#             #     post.save()
#             # except Exception as e:
#             #     print(e)

def spider_page_by_xpath(url, _headers):
    """
    方法一：直接爬取html页面通过xpath解析数据
    此种方法只能爬取每个社区的"最新发布"板块的头20条数据
    """
    res = requests.get(url, headers=_headers)
    if res.status_code == 200:
        res_text = res.text
        sel = Selector(text=res_text)
        post_tags = sel.xpath('//div[contains(@class, "tab-list-item")]')
        print(len(post_tags))
        # print(post_tags.extract())
        for post_tag in post_tags:
            # print(post_tag)
            author_name = post_tag.xpath('.//div[@class="table-item-inner flex1"]/div/a/span/text()').extract()[0]
            author_url = post_tag.xpath('.//div[@class="table-item-inner flex1"]/div/a/@href').extract()[0]
            author_id = re.search('.*/(.*)', author_url).group(1)
            create_at = post_tag.xpath('.//div[@class="table-item-inner flex1"]/div/span/span/text()').extract()[0]
            # 日期数据转换成时间戳
            try:
                create_at = datetime.timestamp(datetime.strptime(create_at, '%Y-%m-%d'))
            except:
                create_at = 0
            try:
                title = post_tag.xpath('.//div[@class="long-text-title"]/text()').extract()[0]
            except:
                title = ''
            try:
                content_url = \
                    post_tag.xpath('.//div[@class="table-item-inner flex1"]/div[2]/div[2]/div/div/a/@href').extract()[0]

                # 将url的帖子id提取出来
                content_id = re.search('.*/(.*)', content_url).group(1)
            except:
                print(post_tag.xpath('.//div').extract()[0])
            rating = post_tag.xpath(
                './/div[@class="table-item-inner flex1"]//div[@class="handle-box"]/div[2]/span/span/text()').extract()[
                0]
            view_num = post_tag.xpath(
                './/div[@class="table-item-inner flex1"]//div[@class="handle-box"]/div[1]/span/span/text()').extract()[
                0]
            comment_num = post_tag.xpath(
                './/div[@class="table-item-inner flex1"]//div[@class="handle-box"]/div[3]/span/span/text()').extract()[
                0]
            if not view_num.isdigit():
                view_num = 0
            else:
                view_num = int(view_num)
            if not comment_num.isdigit():
                comment_num = 0
            else:
                comment_num = int(comment_num)

            try:
                post = Post.create(
                    _id=content_id,
                    author_name=author_name,
                    author_id=author_id,
                    title=title,
                    pcontent='',
                    create_at=create_at,
                    view_num=view_num,
                    comment_num=comment_num,
                    rating=rating
                )

                post.save()

                # 爬取帖子详情

                # 爬取作者信息
            except Exception as e:
                print(e)


def spider(_headers):
    for url in urls_set:
        time.sleep(3)
        # 逐个url爬取
        spider_page_by_xpath(url, headers)




if __name__ == '__main__':
    get_urls()
    # 有提取出数据
    if urls_set:
        spider(headers)


# 请求参数值
# 动态数据请求参数type  1：最新发布 4：最新回复 9：标题 10：阅读量 7：内容评分 2：精选