"""完成自动登录并获取商品的展示视频数据"""

import sys
sys.path.append('/Users/sewellhe/Py_Projects/spider_project/encryption/_captcha')
import time
import base64
import cv2
import re
import pyautogui
import requests

from scrapy import Selector
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pynput.mouse import Controller
from slide_no_source_pic import *
# from utils import smooth_move_to, smooth_move_and_click, find_pic, click_and_drag
from utils import find_pic

ua = UserAgent()

# Options类实例化
chrome_options = Options()

# 1、设置浏览器参数
chrome_options.add_argument('lang=zh_CN.utf-8')
chrome_options.add_argument(f'User-Agent={ua.random}')
chrome_options.add_argument('--start-maximized')
# 不关闭网页
chrome_options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=chrome_options)

# 2、自动登录


time.sleep(1)
# 已登录，用selenium重新读取页面获取js加载完后的html
browser.get('https://item.jd.com/100019667283.html')
html_content = browser.page_source
while True:
    # 等待网页的html和js加载完
    if browser.execute_script("return document.readyState") == 'complete':
        break
    time.sleep(1)

# 将获得的html写入文件，方便调试
with open('check.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
headers_media = {
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

# 获取展示视频的id值
try:
    # infoVideoId是pc_tencent_video_v2
    _re = re.compile(r'infoVideoId\":"([^"]*)"?')
    info_video_id = _re.search(html_content).group(1)

    # mainVideoId是pc_tencent_video_v3
    _re = re.compile(r'mainVideoId\":"([^"]*)"?')
    main_video_id = _re.search(html_content).group(1)
    print(info_video_id, main_video_id)

    id_list = [info_video_id, main_video_id]
    function_id = ['pc_tencent_video_v2', 'pc_tencent_video_v3']

    for i in range(2):
        params_media['vid'] = id_list[i]
        params_media['functionId'] = function_id[i]

        resp = requests.get('https://api.m.jd.com/tencent/video_v3', headers=headers_media
                            , params=params_media)
        print(resp.text)
except:
    print('该商品不存在展示视频....')
