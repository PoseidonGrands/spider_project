"""新的验证码识别，没有原图"""

import base64
import time
import os

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pynput.mouse import Controller, Button

from utils import smooth_move_to, find_pic


def auto_login(url, account_input_xpath, password_input_xpath, login_btn_xpath, username, password, is_wait,
               wait_ele_xpath, big_img_xpath, small_img_xpath, scale):
    # Options类实例化
    chrome_options = Options()
    ua = UserAgent()

    # 设置浏览器参数
    # 启动时设置默认语言为中文 UTF-8
    chrome_options.add_argument('lang=zh_CN.utf-8')
    chrome_options.add_argument(
        f'User-Agent={ua.random}')
    chrome_options.add_argument('--start-maximized')
    # 不关闭网页
    chrome_options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(options=chrome_options)

    browser.get(url)

    # 解析元素，输入账号密码，点击登录
    account_input = browser.find_element(By.XPATH, account_input_xpath)
    password_input = browser.find_element(By.XPATH, password_input_xpath)
    login_btn = browser.find_element(By.XPATH, login_btn_xpath)

    # 用户名
    account_input.send_keys(username)
    # 密码
    password_input.send_keys(password)
    login_btn.click()

    # 是否需要等待验证码元素出现
    if is_wait:
        WebDriverWait(browser, 2).until(
            EC.presence_of_element_located((By.XPATH, wait_ele_xpath))
        )

    # 控制鼠标拖动
    for _ in range(20):
        try:
            bigimg = browser.find_element(By.XPATH, big_img_xpath)
            bigimg_b64 = bigimg.get_attribute('src')
            bigimg_data = base64.b64decode(bigimg_b64.replace('data:image/png;base64,', ''))

            smallimg = browser.find_element(By.XPATH, small_img_xpath)
            smallimg_b64 = smallimg.get_attribute('src')
            smallimg_data = base64.b64decode(smallimg_b64.replace('data:image/png;base64,', ''))
        except Exception as e:
            print('无法获取到验证码图片...')
            break

        directory = os.path.join(os.getcwd(), 'resources')
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open('resources/big_jd.png', 'bw') as f:
            f.write(bigimg_data)

        with open('resources/small_jd.png', 'bw') as f:
            f.write(smallimg_data)

        # 滑块移动距离
        x = find_pic('resources/big_jd.png', 'resources/small_jd.png')
        print(x)
        # 真实尺寸和渲染尺寸有偏差：在浏览器通过调试工具elements将render size / Intrinsic size
        x = (x * (242 / 360)) * scale
        print(f'实际需要移动:{x}')

        offset_x = (smallimg.location.get('x') * scale) + 22
        offset_y = (smallimg.location.get('y') * scale) + 164 + 26
        print(f'offset_x:{offset_x}')
        print(offset_x, offset_y)

        # 移动鼠标
        # 移动是以屏幕左上角为0点，find_element获取到的元素是从浏览器开始渲染页面的左上角为0点，offset_y中有164是浏览器开始渲染点与屏幕左上角点距离
        # 再加26-30是因为find_element获取到的坐标是元素左上角点，所以每个方向都需要加上图标长宽各一半长度
        mouse = Controller()
        smooth_move_to(mouse, offset_x, offset_y)
        # 按下鼠标左键
        mouse.press(Button.left)
        current_x, current_y = mouse.position
        smooth_move_to(mouse, current_x + x + 20, current_y + 10, duration=1)
        smooth_move_to(mouse, current_x + x + 10, current_y + 5, duration=0.7)
        smooth_move_to(mouse, current_x + x, current_y, duration=0.8)
        # 松开鼠标左键
        mouse.release(Button.left)

        time.sleep(2)
