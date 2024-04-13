from slide_no_source_pic import auto_login

if __name__ == '__main__':
    # 1、测试京东登录
    url = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fitem.jd.com%2F100019667283.html&czLogin=1'
    account_input_xpath = '//input[@clstag="pageclick|keycount|passport_main|click_input_loginname"]'
    password_input_xpath = '//input[@clstag="pageclick|keycount|passport_main|click_input_pwd"]'
    login_btn_xpath = '//div[@class="item item-fore5"]/div'
    username = 'sewellhe'
    password = 'CFhechaohua1.'
    is_wait = True
    wait_ele_xpath = '//div[@class="JDJRV-bigimg"]'
    big_img_xpath = '//div[@class="JDJRV-bigimg"]/img'
    small_img_xpath = '//div[@class="JDJRV-smallimg"]/img'

    auto_login(url, account_input_xpath, password_input_xpath, login_btn_xpath, username, password, is_wait, wait_ele_xpath, big_img_xpath, small_img_xpath, 1)
