import random
import datetime
from selenium import webdriver
from time import sleep

your_account = "前程无忧的用户名"
your_password = "前程无忧的密码"
url = "https://www.51job.com"
# 加启动配置，预防谷歌浏览器安全提示
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# 打开chrome浏览器
browser = webdriver.Chrome(chrome_options=option)
browser.get(url)
# 设置浏览器窗口大小
# browser.set_window_size(1360, 600)
browser.maximize_window()
# 找到登录按钮并点击
sleep(2)
browser.find_element_by_class_name("showLogin").click()
# 输入账号和密码
sleep(3)
username = browser.find_element_by_id("loginname")
sleep(2)
username.send_keys("your_account")
sleep(3)
password = browser.find_element_by_id("password")
sleep(2)
password.send_keys("your_password")
# 点击登录按钮
sleep(3)
ret = browser.find_element_by_id("login_btn").click()
print("登录成功！")
while True:
    # 设置简历刷新间隔时间， 单位为秒
    # 就是随机间隔10-15秒刷新，按需求调整，建议设置长一点，万一被服务器封IP就不好了
    waittime = random.randint(10, 15)
    sleep(int(waittime))
    browser.find_element_by_id("refreshresume").click()
    print("简历 在%s 刷新成功" % datetime.datetime.now())
