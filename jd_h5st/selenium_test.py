"""完成自动登录并获取商品的展示视频数据"""
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pynput.mouse import Controller, Button

from model import *
from utils import slide_no_source_pic, utils


def parse_good(_browser, _good_id):

    """已登录，用selenium读取商品详情页面并获取js加载完后的html"""
    _browser.implicitly_wait(6)
    _browser.get(f'https://item.jd.com/{_good_id}.html')

    # 直接找到元素并点击会被反爬，控制鼠标移动到元素上再按下
    # btn = _browser.find_element(By.XPATH, '//div[@id="choose-attr-1"]/div[2]/div[2]')
    # mouse = Controller()
    # utils.smooth_move_to(mouse, 94, 87, duration=1)
    # mouse.click(Button.left)

    # 等待直到某个元素可见
    # while True:
    #     try:
    #         WebDriverWait(_browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'prom-item')))
    #         break
    #     except:
    #         _browser.refresh()
    #         time.sleep(10)

    html_content = browser.page_source
    with open('resources/source.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    # name = _browser.find_element(By.XPATH, '')
    # price = _browser.find_element(By.XPATH, '')
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
    # good = Good()
    # good.id = _good_id


    # headers_media = {
    #     'Referer': 'https://item.jd.com/',
    #     'User-Agent': ua.random
    # }
    #
    # params_media = {
    #     'callback': 'jQuery9419606',
    #     'vid': '877299338',
    #     'type': 1,
    #     'from': 1,
    #     'appid': 'item-v3',
    #     'functionId': 'pc_tencent_video_v3'
    # }
    #
    # # 获取展示视频的id值
    # try:
    #     # infoVideoId是pc_tencent_video_v2
    #     _re = re.compile(r'infoVideoId\":"([^"]*)"?')
    #     info_video_id = _re.search(html_content).group(1)
    #
    #     # mainVideoId是pc_tencent_video_v3
    #     _re = re.compile(r'mainVideoId\":"([^"]*)"?')
    #     main_video_id = _re.search(html_content).group(1)
    #     print(info_video_id, main_video_id)
    #
    #     id_list = [info_video_id, main_video_id]
    #     function_id = ['pc_tencent_video_v2', 'pc_tencent_video_v3']
    #
    #     for i in range(2):
    #         params_media['vid'] = id_list[i]
    #         params_media['functionId'] = function_id[i]
    #
    #         resp = requests.get('https://api.m.jd.com/tencent/video_v3', headers=headers_media
    #                             , params=params_media)
    #         print(resp.text)
    # except:
    #     print('该商品不存在展示视频....')


if __name__ == '__main__':
    # 1、自动登录
    url = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fhome.jd.com%2F'
    account_input_xpath = '//input[@clstag="pageclick|keycount|passport_main|click_input_loginname"]'
    password_input_xpath = '//input[@clstag="pageclick|keycount|passport_main|click_input_pwd"]'
    login_btn_xpath = '//div[@class="item item-fore5"]/div'
    username = 'pixlehe'
    password = 'Hua12345678.'
    is_wait = True
    wait_ele_xpath = '//div[@class="JDJRV-bigimg"]'
    big_img_xpath = '//div[@class="JDJRV-bigimg"]/img'
    small_img_xpath = '//div[@class="JDJRV-smallimg"]/img'

    browser = slide_no_source_pic.auto_login('jd', url, account_input_xpath, password_input_xpath, login_btn_xpath,
                                             username, password, is_wait, wait_ele_xpath, big_img_xpath,
                                             small_img_xpath, 1)

    time.sleep(5)
    # 2、解析数据
    parse_good(browser, '100019667283')