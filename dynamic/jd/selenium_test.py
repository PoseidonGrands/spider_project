import base64
import random

import cv2
import pyautogui

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ua = UserAgent()


url = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fitem.jd.com%2F100019667283.html&czLogin=1'
# Options类实例化
chrome_options = Options()

# 设置浏览器参数
# 启动时设置默认语言为中文 UTF-8

chrome_options.add_argument('lang=zh_CN.utf-8')
chrome_options.add_argument('User-Agent=' + ua.random)
chrome_options.add_argument('--start-maximized')
# 不关闭网页
chrome_options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=chrome_options)

browser.get(url)

# 解析元素，输入账号密码，点击登录
account_input = browser.find_element(By.XPATH, '//input[@clstag="pageclick|keycount|passport_main|click_input_loginname"]')
password_input = browser.find_element(By.XPATH, '//input[@clstag="pageclick|keycount|passport_main|click_input_pwd"]')
login_btn = browser.find_element(By.XPATH, '//div[@class="item item-fore5"]/div')

account_input.send_keys('sewellhe')
password_input.send_keys('CFhechaohua1.')
login_btn.click()


def find_pic(target, template):
    """
    :param target: 背景图路径
    :param template: 滑块图片路径
    :return:
    """
    target_rgb = cv2.imread(target)
    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
    template_rgb = cv2.imread(template, 0)
    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)  # 模板匹配，在大图中找小图
    value = cv2.minMaxLoc(res)
    a, b, c, d = value
    if abs(a) >= abs(b):
        distance = c[0]
    else:
        distance = d[0]
    print(value)
    return distance


# 滑动验证码（无原图
# 1、下载原图和缺块
# 图片的html元素点击登录才会出现，等待元素出现再进行出现
WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="JDJRV-bigimg"]'))
)
bigimg_b64 = browser.find_element(By.XPATH, '//div[@class="JDJRV-bigimg"]/img').get_attribute('src')
bigimg_data = base64.b64decode(bigimg_b64.replace('data:image/png;base64,', ''))

smallimg_b64 = browser.find_element(By.XPATH, '//div[@class="JDJRV-smallimg"]/img').get_attribute('src')
smallimg_data = base64.b64decode(smallimg_b64.replace('data:image/png;base64,', ''))

with open('resources/big.png', 'bw') as f:
    f.write(bigimg_data)

with open('resources/small.png', 'bw') as f:
    f.write(smallimg_data)

x = find_pic('big.png', 'small.png')
print(x)
# 在浏览器通过调试工具elements将render size / Intrinsic size
x = x * (242 // 360)

slide_btn = browser.find_element(By.XPATH, '//div[@class="JDJRV-slide-inner JDJRV-slide-btn"]')
# TODO 网页元素位置映射到pyautogui会有一定缩放
offset_x = slide_btn.location.get('x') * 1.30
offset_y = slide_btn.location.get('y') * 1.75

loc_btn = slide_btn.location.copy()
loc_btn['y'] += 285





# account_input.click()
# password_input.click()
# print(account_input.get_attribute('name'))


# # 获取网页的标题内容
# print(driver.title)
# # page_source用于获取网页的Html代码
# print(driver.page_source)
