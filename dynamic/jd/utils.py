import time
import random
import cv2


from pynput.mouse import Controller, Button
from pywinauto import mouse


def smooth_move_to(x, y, duration=1):
    mouse = Controller()
    # 获取当前鼠标位置
    current_x, current_y = mouse.position
    # 计算每步的位移量
    steps = 100  # 设置移动步数
    dx = (x - current_x) / steps
    dy = (y - current_y) / steps
    # 平滑移动鼠标
    for i in range(steps):
        mouse.position = (current_x + dx * i, current_y + dy * i)
        time.sleep(duration / steps)


def smooth_move_and_click(x, y, duration=1):
    mouse = Controller()
    current_x, current_y = mouse.position
    steps = random.randint(60, 100)  # 随机步骤数
    dx = (x - current_x) / steps
    dy = (y - current_y) / steps
    mouse.press(Button.left)
    time.sleep(random.uniform(0.1, 0.3))  # 模拟按下前的短暂停顿

    for i in range(steps):
        if i % 10 == 0:  # 每隔几步随机停顿
            time.sleep(random.uniform(0.02, 0.1))
        jitter = random.uniform(-2, 2)  # 添加随机抖动
        mouse.position = (current_x + dx + jitter, current_y + dy * i + jitter)
        time.sleep(duration / steps)

    mouse.position = (x, y)
    time.sleep(random.uniform(0.1, 0.3))  # 模拟在松开前的短暂停顿
    mouse.release(Button.left)


def click_and_drag(start_x, start_y, end_x, end_y):
    # 鼠标点击
    mouse.click(button='left', coords=(start_x, start_y))
    time.sleep(0.5)  # 等待一段时间确保点击生效

    # 鼠标拖动
    mouse.press(coords=(start_x, start_y))
    mouse.move(coords=(end_x, end_y))
    mouse.release(coords=(end_x, end_y))


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