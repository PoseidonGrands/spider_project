import time
import cv2


def smooth_move_to(mouse, x, y, duration=1):
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