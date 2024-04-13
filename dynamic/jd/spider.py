import json
import requests
import re

from fake_useragent import UserAgent
from scrapy import Selector
from selenium import webdriver


"""找视频链接文件---找异步请求----没找到-----js找----找到对应的视频url请求-----反爬----header加上referer----该文件请求参数构建vid--
# --通过请求路径全局搜索哪个js文件出现该路径----发现preview.js出现该路径，里面构建了请求参数，发现视频请求的url参数最后一个_=id值不重要，
# 关键在于vid-----看vid的值是变量赋予的，看该变量出现的地方，发现使用了一直imageAndVideoJson的值-----全局搜索该值----
发现html文件的script中出现该值-----复制里面的id值，和请求参数的vid值对比，一致
"""
base_url = 'https://api.m.jd.com'
ua = UserAgent()

headers = {
    'User-Agent': ua.random
}
params = {
    'appid': 'item-v3',
    'functionId': 'pc_club_productPageComments',
    'productId': '-1',
    'score': 0,
    'sortType': 5,
    'page': 0,
    'pageSize': 10
}


headers_media = {
        'Cookie': 'unpl=JF8EALVnAGQiaEMGUklXSBFAG18GC1gNThZQa2EMAVhYQwACHlYaEEIbbVdfXg1XFgZzZwRFXVlAVwwQARgiEEptVF9cCkwWCmpmDWRtWSVUa2xQTxVPPV0qCRlxexQDX2Y1VFtYSFIFHAIaERdOVFRfWQ9CFgVrbwBkXGhLXAErMisXEEpcVVZaCUwWM25XB1VcXU9VAhoBHCJbJVwZXlsISBEDaGcEV1pdQlQEHwUSExZPVVFuXDhI; areaId=19; PCSYCityID=CN_440000_440600_0; shshshfpa=38607327-16f7-7df9-7ad8-6ea84246e04b-1712716105; shshshfpx=38607327-16f7-7df9-7ad8-6ea84246e04b-1712716105; TrackID=1ebzJxAJmVIZFHHxqDVQeG08MBVvYWyDQolRrjy_NvZOImsJ0VjCVFyQ2kX4T1ZCQ9X5MUCdB7sUuXpkF_D30I2oIjc60TOgzbKinLxJ0GG9m_FolZGOHzajJiNjHMIEm; thor=7D9969418D057227D8FC95E105F084469D11C2216D1BB65B00E7DA4E7AEDE9EF6B27E2463E7BF715901903790875BA1C754E28EB11E3D26A52C8DADBF4C7C8252F0C0091552E2452ADC181CA0BF37D9769132443608C143859C9BBF64D66181CF36FA47744B409EDA22493AD59D6812C62D2463E3AE756312D4AE73D363B88AD85ABD9991F216D21AC1657282B525117581A2AE2D2C46BC58F8A9A909E625F19; flash=2_FUxwJaYwxDW__TNaH5eQxkvvoIJYnfa5KStsMgbgeDb9h7U6JnTqf4-65bFlBD_UUfFaBctOmOGkPkPdjcFtxnba1SnDo1xagsBxPOzuWds*; pinId=pa4tWnJsGd1DC_RVMtKlP7V9-x-f3wj7; pin=jd_68ee3d1d70512; unick=sewellss; ceshi3.com=203; _tp=WziaMRXHOdX0KTcni7GnpV4L6uq%2FPlfEXZzwt882hqs%3D; _pst=jd_68ee3d1d70512; __jdv=76161171|www.baidu.com|t_1003608409_|tuiguang|9cfcdb2aa3cd4440b578d419e64e03ca|1712716145460; ipLoc-djd=19-1666-36264-59522; user-key=65535e86-c428-4ecd-ba27-6f4449043ca7; cn=150; jsavif=1; shshshfpb=BApXeEIyAyetAlt035LCTTcgRB9_5gFGRBlAwZipj9xJ1MvfCCIC2; token=8430f8f7d4d0cd9decc71d88c0fa4069,3,951552; __tk=yJhdvVbiqgr3IbrbyJh5vMTaIgTtIRKUygh5vMTTyiKtNB9hIBhRug9TJBKAHJFBIDrtOBF4,3,951552; __jda=181111935.17127161026481056807594.1712716102.1712721373.1712794609.3; __jdb=181111935.8.17127161026481056807594|3.1712794609; __jdc=181111935',
        'Referer': 'https://item.jd.com/',
        'User-Agent': ua.random
    }

params_media = {
    'callback': 'jQuery9419606',
    'vid': '877299338',
    'type': 1,
    'from': 1,
    'appid': 'item-v3',
    'functionId': 'pc_tencent_video_v3'
}
    # resp = requests.get('https://api.m.jd.com/tencent/video_v3')


def parse_media_id(html):
    _re = re.compile(r'hotKey\s*')
    data = _re.search(html)
    pass


if __name__ == '__main__':
    resp = requests.get('https://item.jd.com/100019667283.html', headers=headers)
    if resp.status_code == 200:
        print(resp.text)
        # parse_media_id(resp.text)


