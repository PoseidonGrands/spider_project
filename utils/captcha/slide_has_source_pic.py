from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ua = UserAgent()

url = ''
username = ''
password = ''

chrome_options = Options()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('lang=zh_CH.utf-8')
chrome_options.add_argument(f'User-Agent={ua.random}')
chrome_options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=chrome_options)

browser.get(url)

# 获取控件输入账号密码，点击登录
username_input = browser.find_element(By.XPATH, '')
password_input = browser.find_element(By.XPATH, '')
login_btn = browser.find_element(By.XPATH, '')
username_input.send_keys(username)
password_input.send_keys(password)
login_btn.click()

# 等待验证码html元素出现
WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.XPATH, ''))
)

# 获取原图，保存
source_img = browser.find_element(By.XPATH, '')
big_img = browser.find_element(By.XPATH, '')
small_img = browser.find_element(By.XPATH, '')

with open() as f:
    pass
with open() as f:
    pass
