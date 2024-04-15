
"""
没有实现爬取其他社区 sha256加密，其中的参数X-Ca-Nonce无法获取，x-ca-key和appkey都能通过xpath获取
"""

import base64

import requests
import re
import os
import time
import execjs
import hmac
import hashlib
from selenium import webdriver

_re = re.compile(r'"communityHomePage":\s*"([^"]+)"')
# data = requests.get('https://bbs.csdn.net/forums/paddlepaddle?category=10001')
# # print(data.text)
# nav_list = _re.findall(data.text)
# # print(len(nav_list))
#
#
# # 初始化文件
# path = os.path.join(os.getcwd(), 'urls_nav_recommend.txt')
# if os.path.exists(path):
#     os.remove(path)
#
# # 存储到文件
# with open(path, 'a') as f:
#     for url in nav_list:
#         decoded_url = requests.utils.unquote(url.replace('\\u002F', '/'))
#         f.write(decoded_url + '\n')

# for i in range(1, 37):
#     # time.sleep(2)
#     base_url = 'https://bizapi.csdn.net/community-cloud/v1/homepage/community/by/tag'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/118.0.0.0 Safari/537.36 ',
#         'X-Ca-Key': '203899271',
#         'X-Ca-Nonce': '8e1265dd-11fd-4e6d-b556-cd7fd765eecf',
#         'X-Ca-Signature': 'ATKdOel4tWBmdhplKefl006Hl2aD3dY5KgpzY9Jcd1k=',
#         'X-Ca-Signature-Headers': 'x-ca-key,x-ca-nonce'
#     }
#     params = {
#         'deviceType': 'PC',
#         'tagId': i
#     }
#     resp = requests.get(base_url, headers=headers, params=params)
#     print(resp.text)
#     if resp.status_code == 200:
#         data = resp.json()['data']
#         print(data)
#         for i in data:
#             print(i['url'])
#     break
# a = 'GET'
#     c = 'https://bizapi.csdn.net/community-cloud/v1/community/task/recent'
#     t = 'application/json, text/plain, */*'
#     u = {'communityID': 3276}
#     n = ''
#     i = ''
#     s = app_secret
#     headers = {
#         "common": {
#             "Accept": "application/json, text/plain, */*"
#         },
#         "delete": {},
#         "get": {},
#         "head": {},
#         "post": {
#             "Content-Type": "application/json;charset=UTF-8"
#         },
#         "put": {
#             "Content-Type": "application/x-www-form-urlencoded"
#         },
#         "patch": {
#             "Content-Type": "application/x-www-form-urlencoded"
#         },
#         "X-Ca-Key": x_ca_key,
#         "X-Ca-Nonce": x_ca_nonce
#     }
#


    # ctx = execjs.compile(js_code)
    # x_ca_nonce = ctx.call("h", {
    #     'method': a,
    #     'url': c,
    #     'accept': t,
    #     'params': u,
    #     'date': n,
    #     'contentType': i,
    #     'headers': headers,
    #     'appSecret': s
    # })
    # print(x_ca_nonce)




if __name__ == '__main__':
    url = 'https://csdnimg.cn/release/cmsfe/public/js/chunk/tpl/ccloud-index/index.9ec42fc7.js'
    # url = 'https://bbs.csdn.net/forums/unitygame?category=7'
    res = requests.get(url).text
    # _re = re.compile('''e\.headers\["X-Ca-Key"\]\s*=(.*)''')
    # _re = re.compile('''e.headers\[\"X-Ca-Signature\"\]=([(^")])''')
    # _key = _re.search(res)
    # print(_key)

    # driver = webdriver.Chrome()
    # driver.get(url)
    #
    # # script = 'console.log(e["headers"]["X-Ca-Key"]);'
    # script = 'console.log(f());'
    # value = driver.execute_script(script)
    #
    # # 打印输出值
    # print("X-Ca-Key 的值为:", value)

    # 关闭 WebDriver 实例
    # driver.quit()
    text = """
    if (p ? (r = p.appKey,
            s = p.appSecret) : (r = 203899271,
            s = "bK9jk5dBEtjauy6gXL7vZCPJ1fOy076H"),
            a = a.toUpperCase(),
    """
    # _re = re.compile(r'\(r\s*=\s*p.appKey,\s*s\s*=\s*p.appSecret\)\s*:\s*\(r\s*=\s*([0-9]*),\s*s\s*=\s*"([a-zA-Z0-9]*)"')
    # x_ca_key = _re.search(res).group(1)
    # app_secret = _re.search(res).group(2)
    #
    # print(x_ca_key)
    #
    # with open("get_data.js", encoding='utf-8') as f:
    #     js_code = f.read()
    #
    # ctx = execjs.compile(js_code)
    # x_ca_nonce = ctx.call("f")
    # print(x_ca_nonce)
    #
    #
    #
    # data = f"GET\napplication/json, text/plain, */*\n\nx-ca-key:{x_ca_key}\nx-ca-nonce:{x_ca_nonce}\n/community-cloud/v1/homepage/community/by/tag?deviceType=PC&tagId=2"
    #
    # hmac_sha256 = hmac.new(app_secret.encode('utf-8'), data.encode('utf-8'), digestmod=hashlib.sha256)
    # digest = hmac_sha256.digest()
    #
    # # 进行 Base64 编码
    # x_ca_signature = base64.b64encode(digest).decode('utf-8')
    #
    # print("加密后的数据：", x_ca_signature)
    #
    # url = 'https://bizapi.csdn.net/community-cloud/v1/homepage/community/by/tag?deviceType=PC&tagId=2'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                   'Chrome/118.0.0.0 Safari/537.36 ',
    #     'X-Ca-Key': x_ca_key,
    #     'X-Ca-Nonce': x_ca_nonce,
    #     'X-Ca-Signature': x_ca_signature,
    #     'X-Ca-Signature-Headers': 'x-ca-key,x-ca-nonce'
    # }
    #
    # resp = requests.get(url, headers=headers)
    # print(resp.text)
