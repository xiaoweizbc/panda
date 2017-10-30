# coding=utf-8
from selenium import webdriver
import time

# driver = webdriver.Chrome()  # 依赖于chromedriver.exe（s7）
# driver.get("http://www.panda.tv/6666")
# driver.maximize_window()  # chrome版本要低于55，否则报错

# driver = webdriver.Firefox()  # 依赖于geckodriver.exe
# driver.get("http://www.panda.tv/6666")

driver = webdriver.PhantomJS()  # 依赖于phantomjs.exe
driver.get("http://www.panda.tv/6666")
driver.set_window_size(1920, 1080)  # 解决发弹幕时phantomjs报错

driver.implicitly_wait(15)
print(driver.title)

try:
    driver.find_element_by_link_text("登录").click()  # 点击“登录”按钮，随后弹出小窗口
    time.sleep(3)  # 等待页面加载

    driver.find_element_by_xpath('//*[@id="ruc-dialog-container"]/div[1]/div[2]/div/div[1]/div/input').send_keys("1361007****")  # 在小窗口输入用户名即手机
    driver.find_element_by_xpath('//*[@id="ruc-dialog-container"]/div[1]/div[2]/div/div[2]/input').send_keys("******")  # 在小窗口输入密码
    driver.find_element_by_xpath('//*[@id="ruc-dialog-container"]/div[1]/div[2]/div/div[6]').click()  # 点击“立即登录”按钮
    time.sleep(3)  # 等待页面加载

    try:
        # 若登陆需要手机验证码，则加上下列代码
        driver.find_element_by_xpath('//*[@id="ruc-dialog-container"]/div[1]/div[2]/div/div[3]/a').click()  # 点击“发送验证码”按钮
        code = raw_input("输入验证码：")
        driver.find_element_by_xpath('//*[@id="ruc-dialog-container"]/div[1]/div[2]/div/div[3]/input').send_keys(code)  # 输入验证码
        driver.find_element_by_xpath('//*[@id="ruc-dialog-container"]/div[1]/div[2]/div/div[6]').click()  # 点击“立即登录”按钮
        time.sleep(3)  # 等待页面加载
    except Exception as e:
        print "不用验证手机就可以登录了"
        # print e

    print("登录成功")
    raw_input("回车即可发送弹幕")

    while 1:
        try:
            # word = raw_input("输入您要发的弹幕回车：")  # 自定义弹幕
            word = u"世界第一上单pdd！"
            driver.find_element_by_xpath('//*[@id="main-container"]/div[3]/div[4]/div[2]/div[1]/textarea').send_keys(word)  # 输入弹幕
            driver.find_element_by_xpath("//*[@id='main-container']/div[3]/div[4]/div[2]/div[2]").click()  # 点击“发送”
            print(u"(%s)发送<%s>成功！" % (time.strftime("%Y/%m/%d-%H:%M:%S"), word))
            time.sleep(3)  # 三秒发一次弹幕
        except Exception as e:
            print(u"({})发送<{}>失败！".format(time.strftime("%Y/%m/%d-%H:%M:%S"), word))
            print(e)

    driver.quit()
except Exception as e:
    print(e)
