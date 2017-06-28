#encoding=utf-8
import os
import traceback

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

from Util import FormatTime
from Util.ObjectMap import *
from ProjectVar import var

# 定义全局的浏览器driver变量
driver = None
wait_time = 0.3

def open_browser(broswerName, *args):
    global driver
    broswerName = broswerName.strip().lower()
    # print broswerName
    try:
        if broswerName == 'ie':
            driver = webdriver.Ie(executable_path=var.ieDriverFilePath)
        elif broswerName == 'firefox':
            driver = webdriver.Firefox(executable_path=var.firefoxDriverFilePath)
        elif broswerName == 'chrome':
            # 创建Chrome浏览器的一个Options实例对象
            chrome_options = Options()
            # 添加屏蔽--ignore-certificate-errors提示信息的设置参数项
            chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            driver = webdriver.Chrome(executable_path=var.chromeDriverFilePath, chrome_options = chrome_options)
        else:
            raise ValueError("broswerName error: " + broswerName)
        driver.maximize_window()
    except Exception, e:
        raise e

def visit_url(url, *args):
    global driver
    try:
        driver.get(url)
    except Exception, e:
        raise e

def close_browser():
    global driver
    try:
        driver.quit()
    except Exception, e:
        raise e

def sleep(second, *args):
    try:
        time.sleep(float(second))
    except Exception, e:
        raise e

def enter_frame(locatorMethod, locatorExpression, *args):
    global driver
    try:
        element = getElement(driver,locatorMethod,locatorExpression)
        sleep(wait_time)
        driver.switch_to.frame(element)
    except Exception, e:
        raise e

def input(locatorMethod, locatorExpression, content, *args):
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        sleep(wait_time)
        element.send_keys(content.decode())
    except Exception, e:
        raise e

def click(locatorMethod, locatorExpression, *args):
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        sleep(wait_time)
        element.click()
    except Exception, e:
        raise e

def assert_In(expected_word, source=None, *args):
    try:
        if source == None:
            source = driver.page_source
        assert expected_word in source
    except Exception, e:
        raise e

def login(usernameAndpassword, *args):
    u"""登录"""
    username, password = usernameAndpassword.split('||')
    open_browser('Chrome')
    visit_url("http:\\mail.126.com")
    sleep(3)
    enter_frame('id', 'x-URS-iframe')
    sleep(2)
    input_string('xpath', "//input[@name='email']", username)
    input_string('xpath', "//input[@name='password']", password)
    click('id', "dologin")
    click('xpath', "//a[text()='继续登录']")
    sleep(3)
    # close_browser()
    assert_In(u"退出")

def addcontacts(name, mail, mobile, comment, is_set_star):
    u"""新建联系人"""
    click('xpath', "//div[@role='toolbar']//span[text()='新建联系人']")
    input_string('xpath', "//a[@title='编辑详细姓名']/preceding-sibling::div/input", name)
    input_string('xpath', "//*[@id='iaddress_MAIL_wrap']//input", mail)
    if is_set_star:
        click('xpath', "//span[text()='设为星标联系人']/preceding-sibling::span/b")
    input_string('xpath', "//*[@id='iaddress_TEL_wrap']//dd//input", mobile)
    input_string('xpath', "//textarea", comment)
    click('xpath', "//span[.='确 定']")

def screen_shot(dir='ErrorPicture'):
    u"""截图"""
    try:
        if dir == 'ErrorPicture':
            file_dir = os.path.join(var.ErrorPicturePath, FormatTime.date_slash())
        elif dir == 'CapturePicture':
            file_dir = os.path.join(var.CapturePicturePath, FormatTime.date_slash())
        else:
            raise ValueError
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        # 命名方式：HHMMSS.jpg
        file_name = FormatTime.time_slash() + '.jpg'
        file_path = os.path.join(file_dir, file_name)
        driver.get_screenshot_as_file(file_path)
        return file_path
    except:
        print traceback.format_exc()

if __name__ == '__main__':
    # 登录
    login("sjjm0001||11111q")
    # 点击通讯录
    click('xpath', "//div[text()='通讯录']")
    # 新建联系人
    addcontacts(u"李旺", u"liwang@126.com", u"18888888888", u"光荣之路测试开发班", True)
    sleep(1)
    assert_In(u"hahaha")
    # close_browser()
