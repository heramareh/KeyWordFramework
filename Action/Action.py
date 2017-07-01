#encoding=utf-8
import os
import time
import traceback
import win32api
import win32clipboard
import Image
import win32con
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Util import FormatTime
from Util.ObjectMap import *
from ProjectVar import var

# 定义全局的浏览器driver变量
driver = None
# 定义键盘按键code
VK_CODE = {
    'backspace': 0x08, '  ': 0x08, ' ': 0x08,
    'tab': 0x09,
    'clear': 0x0C,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'caps_lock': 0x14,
    'esc': 0x1B,
    'spacebar': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'select': 0x29,
    'print': 0x2A,
    'execute': 0x2B,
    'print_screen': 0x2C,
    'ins': 0x2D,
    'del': 0x2E,
    'help': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 'g': 0x47, 'h': 0x48, 'i': 0x49, 'j': 0x4A,
    'k': 0x4B, 'l': 0x4C, 'm': 0x4D, 'n': 0x4E, 'o': 0x4F, 'p': 0x50, 'q': 0x51, 'r': 0x52, 's': 0x53, 't': 0x54,
    'u': 0x55, 'v': 0x56, 'w': 0x57, 'x': 0x58, 'y': 0x59, 'z': 0x5A,
    'A': 0x41, 'B': 0x42, 'C': 0x43, 'D': 0x44, 'E': 0x45, 'F': 0x46, 'G': 0x47, 'H': 0x48, 'I': 0x49, 'J': 0x4A,
    'K': 0x4B, 'L': 0x4C, 'M': 0x4D, 'N': 0x4E, 'O': 0x4F, 'P': 0x50, 'Q': 0x51, 'R': 0x52, 'S': 0x53, 'T': 0x54,
    'U': 0x55, 'V': 0x56, 'W': 0x57, 'X': 0x58, 'Y': 0x59, 'Z': 0x5A,
    'numpad_0': 0x60,
    'numpad_1': 0x61,
    'numpad_2': 0x62,
    'numpad_3': 0x63,
    'numpad_4': 0x64,
    'numpad_5': 0x65,
    'numpad_6': 0x66,
    'numpad_7': 0x67,
    'numpad_8': 0x68,
    'numpad_9': 0x69,
    'multiply_key': 0x6A,
    'add_key': 0x6B,
    'separator_key': 0x6C,
    'subtract_key': 0x6D,
    'decimal_key': 0x6E,
    'divide_key': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'F13': 0x7C,
    'F14': 0x7D,
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F18': 0x81,
    'F19': 0x82,
    'F20': 0x83,
    'F21': 0x84,
    'F22': 0x85,
    'F23': 0x86,
    'F24': 0x87,
    'num_lock': 0x90,
    'scroll_lock': 0x91,
    'left_shift': 0xA0,
    'right_shift ': 0xA1,
    'left_control': 0xA2,
    'right_control': 0xA3,
    'left_menu': 0xA4,
    'right_menu': 0xA5,
    'browser_back': 0xA6,
    'browser_forward': 0xA7,
    'browser_refresh': 0xA8,
    'browser_stop': 0xA9,
    'browser_search': 0xAA,
    'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC,
    'volume_mute': 0xAD,
    'volume_Down': 0xAE,
    'volume_up': 0xAF,
    'next_track': 0xB0,
    'previous_track': 0xB1,
    'stop_media': 0xB2,
    'play/pause_media': 0xB3,
    'start_mail': 0xB4,
    'select_media': 0xB5,
    'start_application_1': 0xB6,
    'start_application_2': 0xB7,
    'attn_key': 0xF6,
    'crsel_key': 0xF7,
    'exsel_key': 0xF8,
    'play_key': 0xFA,
    'zoom_key': 0xFB,
    'clear_key': 0xFE,
    '=': 0x3d,
    '+': 0x2B,
    ',': 0x2C,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    '`': 0xC0,
    ';': 0xBA,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE,
    '`': 0xC0,
    "@": 0x40}

def open_browser(broswerName, *args):
    u"""打开浏览器"""
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
    except Exception, e:
        raise e

def visit_url(url, *args):
    u"""访问url"""
    global driver
    try:
        driver.get(url)
    except Exception, e:
        raise e

def browser_back():
    u"""浏览器后退"""
    global driver
    try:
        driver.back()
    except Exception, e:
        raise e

def browser_forward():
    u"""浏览器前进"""
    global driver
    try:
        driver.forward()
    except Exception, e:
        raise e

def browser_refresh():
    u"""浏览器刷新"""
    global driver
    try:
        driver.refresh()
    except Exception, e:
        raise e

def browser_window_max():
    u"""浏览器窗口最大化"""
    global driver
    try:
        driver.maximize_window()
    except Exception, e:
        raise e

def set_browser_window_position(x, y):
    u"""设置浏览器窗口位置"""
    global driver
    try:
        driver.set_window_position(x = x, y = y)
    except Exception, e:
        raise e

def set_browser_window_size(w, h):
    u"""设置浏览器窗口大小"""
    global driver
    try:
        driver.set_window_size(width=w, height=h)
    except Exception, e:
        raise e

def get_window_title():
    u"""获取页面的title属性"""
    global driver
    try:
        return driver.title
    except Exception, e:
        raise e

def get_page_source():
    u"""获取页面HTML源码"""
    global driver
    try:
        return driver.page_source
    except Exception, e:
        raise e

def get_current_url():
    u"""获取当前页面的url地址"""
    global driver
    try:
        return driver.current_url
    except Exception, e:
        raise e

def get_current_window_handle():
    u"""获取当前窗口句柄"""
    global driver
    try:
        return driver.current_window_handle
    except Exception, e:
        raise e

def get_window_handles():
    u"""获取所有窗口句柄"""
    global driver
    try:
        return driver.window_handles
    except Exception, e:
        raise e

def switch_to_window(window_handle):
    u"""根据句柄切换窗口"""
    global driver
    try:
        driver.switch_to.window(window_handle)
    except Exception, e:
        raise e

def close_browser():
    u"""关闭浏览器"""
    global driver
    try:
        driver.quit()
    except Exception, e:
        raise e

def set_page_load_time(wait_time):
    u"""设置页面加载时间"""
    global driver
    try:
        driver.set_page_load_timeout(wait_time)
    except Exception, e:
        raise e

def sleep(second, *args):
    u"""等待"""
    try:
        time.sleep(float(second))
    except Exception, e:
        raise e

def enter_frame(locatorMethod, locatorExpression, *args):
    u"""切换进frame"""
    global driver
    try:
        element = getElement(driver,locatorMethod,locatorExpression)
        driver.switch_to.frame(element)
    except Exception, e:
        raise e

def switch_to_default():
    u"""切换到默认页面"""
    global driver
    try:
        driver.switch_to.default_content()
    except Exception, e:
        raise e

def input(locatorMethod, locatorExpression, content, *args):
    u"""输入内容"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        element.send_keys(content.decode())
    except Exception, e:
        raise e

def clear(locatorMethod, locatorExpression, *args):
    u"""清空内容"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        element.clear()
    except Exception, e:
        raise e

def click(locatorMethod, locatorExpression, *args):
    u"""单机元素"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        element.click()
    except Exception, e:
        raise e

def double_click(locatorMethod, locatorExpression, *args):
    u"""双击元素"""
    global driver
    try:
        action_chains = ActionChains(driver)
        element = getElement(driver, locatorMethod, locatorExpression)
        action_chains.double_click(element).perform()
    except Exception, e:
        raise e

def mouse_right_click(locatorMethod, locatorExpression, *args):
    u"""模拟鼠标右键点击操作"""
    global driver
    try:
        action_chains = ActionChains(driver)
        element = getElement(driver, locatorMethod, locatorExpression)
        action_chains.context_click(element).perform()
    except Exception, e:
        raise e

def mouse_left_click(locatorMethod, locatorExpression, *args):
    u"""模拟鼠标左键点击操作"""
    global driver
    try:
        action_chains = ActionChains(driver)
        element = getElement(driver, locatorMethod, locatorExpression)
        action_chains.click_and_hold(element).perform()
        action_chains.release(element).perform()
    except Exception, e:
        raise e

def move_mouse_to_element(locatorMethod, locatorExpression, *args):
    u"""移动鼠标箭头到指定元素上"""
    global driver
    try:
        action_chains = ActionChains(driver)
        element = getElement(driver, locatorMethod, locatorExpression)
        action_chains.move_to_element(element).perform()
    except Exception, e:
        raise e

def send_Key(locatorMethod, locatorExpression, key, *args):
    u"""模拟键盘按键操作"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        keyCode = eval("Keys." + key.strip().upper())
        element.send_keys(keyCode)
    except Exception, e:
        raise e

def get_element_tag_name(locatorMethod, locatorExpression, *args):
    u"""获取元素标签名"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        return element.tag_name
    except Exception, e:
        raise e

def get_element_size(locatorMethod, locatorExpression, *args):
    u"""获取元素大小，返回一个字典：{'width': xxx, 'height': xxx}"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        return element.size
    except Exception, e:
        raise e

def get_element_location(locatorMethod, locatorExpression, *args):
    u"""获取元素位置坐标，返回一个字典：{'y': xxx, 'x': xxx}"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        return element.location
    except Exception, e:
        raise e

def get_element_attribute(locatorMethod, locatorExpression, attribute_name, *args):
    u"""获取元素属性值"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        return element.get_attribute(attribute_name)
    except Exception, e:
        raise e

def get_element_css_attr(locatorMethod, locatorExpression, css_attr_name, *args):
    u"""获取元素css属性值"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        return element.value_of_css_property(css_attr_name)
    except Exception, e:
        raise e

def get_select_options_texts(locatorMethod, locatorExpression, *args):
    u"""获取select所有选项的文本"""
    global driver
    try:
        select = Select(getElement(driver, locatorMethod, locatorExpression))
        all_options = select.options
        texts = []
        for option in all_options:
            texts.append(option.text)
        return texts
    except Exception, e:
        raise e

def get_select_options_values(locatorMethod, locatorExpression, *args):
    u"""获取select所有选项的value"""
    global driver
    try:
        select = Select(getElement(driver, locatorMethod, locatorExpression))
        all_options = select.options
        values = []
        for option in all_options:
            values.append(option.get_attribute('value'))
        return values
    except Exception, e:
        raise e

def get_default_select_text(locatorMethod, locatorExpression, *args):
    u"""获取默认选择项文本"""
    global driver
    try:
        select = Select(getElement(driver, locatorMethod, locatorExpression))
        return select.first_selected_option.text
    except Exception, e:
        raise e

def get_default_select_value(locatorMethod, locatorExpression, *args):
    u"""获取默认选择项文本"""
    global driver
    try:
        select = Select(getElement(driver, locatorMethod, locatorExpression))
        return select.first_selected_option.get_attribute('value')
    except Exception, e:
        raise e

def select_option_by_text(locatorMethod, locatorExpression, option_text, *args):
    u"""选择下拉项根据文本"""
    global driver
    try:
        select = Select(getElement(driver, locatorMethod, locatorExpression))
        if option_text != select.first_selected_option.text:
            select.select_by_visible_text(option_text)
    except Exception, e:
        raise e

def deselect_option_by_text(locatorMethod, locatorExpression, option_text, *args):
    u"""取消勾选选中项根据文本"""
    global driver
    try:
        select = Select(getElement(driver, locatorMethod, locatorExpression))
        select.deselect_by_visible_text(option_text)
    except Exception, e:
        raise e

def select_option_by_value(locatorMethod, locatorExpression, option_value, *args):
    u"""选择下拉项根据value"""
    global driver
    try:
        select = Select(getElement(driver, locatorMethod, locatorExpression))
        if option_value != select.first_selected_option.get_attribute('value'):
            select.select_by_visible_text(option_value)
    except Exception, e:
        raise e

def deselect_option_by_value(locatorMethod, locatorExpression, option_value, *args):
    u"""取消勾选选中项根据value"""
    global driver
    try:
        select = Select(getElement(driver, locatorMethod, locatorExpression))
        select.deselect_by_value(option_value)
    except Exception, e:
        raise e

def select_option_by_index(locatorMethod, locatorExpression, option_index, *args):
    u"""选择下拉项根据index"""
    global driver
    try:
        select = Select(getElement(driver, locatorMethod, locatorExpression))
        select.select_by_index(option_index)
    except Exception, e:
        raise e

def deselect_option_by_index(locatorMethod, locatorExpression, option_index, *args):
    u"""取消勾选选中项根据index"""
    global driver
    try:
        select = Select(getElement(driver, locatorMethod, locatorExpression))
        select.deselect_by_index(option_index)
    except Exception, e:
        raise e

def deselect_all(locatorMethod, locatorExpression, *args):
    u"""取消勾选所有选中项"""
    global driver
    try:
        select = Select(getElement(driver, locatorMethod, locatorExpression))
        select.deselect_all()
    except Exception, e:
        raise e

def is_displayed(locatorMethod, locatorExpression, *args):
    u"""判断元素是否可见"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        return element.is_displayed()
    except Exception, e:
        raise e

def is_enabled(locatorMethod, locatorExpression, *args):
    u"""判断元素是否可操作"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        return element.is_enabled()
    except Exception, e:
        raise e

def is_selected(locatorMethod, locatorExpression, *args):
    u"""判断元素是否被选中"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        return element.is_selected()
    except Exception, e:
        raise e

def is_present(locatorMethod, locatorExpression, *args):
    u"""判断元素是否存在"""
    global driver
    try:
        getElement(driver, locatorMethod, locatorExpression)
    except Exception, e:
        return False
    else:
        return True

def implicitly_wait(wait_time):
    u"""设置隐式等待时间"""
    global driver
    try:
        driver.implicitly_wait(wait_time)
    except Exception, e:
        raise e

def get_alert_text():
    u"""获取弹窗中的内容"""
    global driver
    try:
        alert = driver.switch_to_alert()
        return alert.text
    except Exception, e:
        raise e

def close_alert_by_accept():
    u"""点击确定关闭弹窗"""
    global driver
    try:
        alert = driver.switch_to_alert()
        alert.accept()
    except Exception, e:
        raise e

def close_alert_by_dismiss():
    u"""点击取消关闭弹窗"""
    global driver
    try:
        alert = driver.switch_to_alert()
        alert.dismiss()
    except Exception, e:
        raise e

def select_checkBox(locatorMethod, locatorExpression, *args):
    u"""勾选复选框"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        if not element.is_selected():
            element.click()
    except Exception, e:
        raise e

def deselect_checkBox(locatorMethod, locatorExpression, *args):
    u"""取消勾选复选框"""
    global driver
    try:
        element = getElement(driver, locatorMethod, locatorExpression)
        if element.is_selected():
            element.click()
    except Exception, e:
        raise e

def drag_element(locatorMethod, locatorExpression, x, y, *args):
    u"""拖拽元素"""
    global driver
    try:
        action_chains = ActionChains(driver)
        element = getElement(driver, locatorMethod, locatorExpression)
        action_chains.drag_and_drop_by_offset(element, x, y).perform()
    except Exception, e:
        raise e

def key_down(key_name):
    u"""模拟键盘压下按键"""
    try:
        win32api.keybd_event(VK_CODE[key_name], 0, 0, 0)
    except Exception, e:
        raise e

def key_up(key_name):
    u"""模拟键盘释放按键"""
    try:
        win32api.keybd_event(VK_CODE[key_name], 0, win32con.KEYEVENTF_KEYUP, 0)
    except Exception, e:
        raise e

def ctrl_a():
    u"""组合按键Ctrl+A"""
    try:
        key_down('ctrl')
        key_down('a')
        key_up('a')
        key_up('ctrl')
    except Exception, e:
        raise e

def ctrl_c():
    u"""组合按键Ctrl+C"""
    try:
        key_down('ctrl')
        key_down('c')
        key_up('c')
        key_up('ctrl')
    except Exception, e:
        raise e

def ctrl_x():
    u"""组合按键Ctrl+X"""
    try:
        key_down('ctrl')
        key_down('x')
        key_up('x')
        key_up('ctrl')
    except Exception, e:
        raise e

def ctrl_v():
    u"""组合按键Ctrl+V"""
    try:
        key_down('ctrl')
        key_down('v')
        key_up('v')
        key_up('ctrl')
    except Exception, e:
        raise e

def press_key_ctrl(key):
    u"""执行ctrl的组合键"""
    try:
        global driver
        ActionChains(driver).key_down(Keys.CONTROL).send_keys(key).key_up(Keys.CONTROL).perform()
    except Exception, e:
        raise e

def press_key_shift(key):
    u"""执行shift的组合键"""
    try:
        global driver
        ActionChains(driver).key_down(Keys.SHIFT).send_keys(key).key_up(Keys.SHIFT).perform()
    except Exception, e:
        raise e

def get_clipboard_text():
    u"""读取剪切板内容"""
    try:
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData(win32con.CF_TEXT)
        win32clipboard.CloseClipboard()
        return text
    except Exception, e:
        raise e

def set_clipboard_text(text):
    u"""设置剪贴板内容"""
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
        win32clipboard.CloseClipboard()
    except Exception, e:
        raise e

def execute_script(js):
    u"""执行js语句"""
    global driver
    try:
        driver.execute_script(js)
    except Exception, e:
        raise e

def get_cookies():
    u"""获取当前页面下所有的cookies，并返回给它们所在域、name、value、有效期和路径"""
    global driver
    try:
        content = []
        cookies = driver.get_cookies()
        for cookie in cookies:
            content.append("%s -> %s -> %s -> %s -> %s" % (cookie['domain'], cookie["name"], cookie["value"], cookie["expiry"], cookie["path"]))
        return content
    except Exception, e:
        raise e

def get_cookie_by_name(name):
    global driver
    try:
        cookie = driver.get_cookie(name)
        return "%s -> %s -> %s -> %s -> %s" % (cookie['domain'], cookie["name"], cookie["value"], cookie["expiry"], cookie["path"])
    except Exception, e:
        raise e

def delete_cookie_by_name(name):
    global driver
    try:
        driver.delete_cookie(name)
    except Exception, e:
        raise e

def delete_cookies():
    u"""删除所有cookies"""
    global driver
    try:
        driver.delete_all_cookies()
    except Exception, e:
        raise e

def add_cookie(cookie):
    u"""添加自定义cookie信息，cookie：{'name': 'xxxx', 'value': 'xxxx'}"""
    global driver
    try:
        driver.add_cookie(eval(cookie))
    except Exception, e:
        raise e

def assert_In(expected_word, source=None, *args):
    u"""断言expected_word在source中"""
    global driver
    try:
        if source == None:
            source = driver.page_source
        assert expected_word in source
    except Exception, e:
        raise e

def scroll_bar(x="document.body.scrollWidth", y="document.body.scrollHeight"):
    u"""操作滚动条"""
    try:
        execute_script("window.scrollTo(" + x + "," + y + ");")
    except Exception, e:
        raise e

def kill_process(process_name):
    u"""根据进程名，结束进程"""
    try:
        os.system("taskkill /F /iM " + process_name)
    except Exception, e:
        raise e

def kill_browser_process():
    u"""结束浏览器进程"""
    try:
        os.system("taskkill /F /iM firefox.exe")
        os.system("taskkill /F /iM iexplore.exe")
        os.system("taskkill /F /iM chrome.exe")
    except Exception, e:
        raise e

def add_attribute(locatorMethod, locatorExpression, attribute_name, value):
    u"""向元素标签中添加新属性"""
    global driver
    try:
        driver.execute_script("arguments[0].%s=arguments[1]" % attribute_name, getElement(driver, locatorMethod, locatorExpression), value)
    except Exception, e:
        raise e

def set_attribute(locatorMethod, locatorExpression, attribute_name, value):
    u"""设置元素标签中属性值"""
    global driver
    try:
        driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", getElement(driver, locatorMethod, locatorExpression), attribute_name, value)
    except Exception, e:
        raise e

def get_attribute(locatorMethod, locatorExpression, attribute_name):
    u"""获取元素标签中属性值"""
    global driver
    try:
        getElement(driver, locatorMethod, locatorExpression).get_attribute(attribute_name)
    except Exception, e:
        raise e

def remove_attribute(locatorMethod, locatorExpression, attribute_name):
    u"""删除元素标签中属性"""
    global driver
    try:
        driver.execute_script("arguments[0].removeAttribute(arguments[1])", getElement(driver, locatorMethod, locatorExpression), attribute_name)
    except Exception, e:
        raise e

def high_light_element(locatorMethod, locatorExpression, *args):
    u"""高亮显示元素"""
    global driver
    try:
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", getElement(driver, locatorMethod, locatorExpression), "background:green; border:2px solid red;")
    except Exception, e:
        raise e

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

def make_regalur_image(img, size=(256, 256)):
    # 将图片尺寸强制重置为指定的size大小
    # 然后再将其转换成RGB值
    return img.resize(size).convert('RGB')

def split_image(img, part_size=(64, 64)):
    # 将图片按给定大小切分
    w, h = img.size
    pw, ph = part_size
    assert w % pw == h % ph == 0
    return [img.crop((i, j, i + pw, j + ph)).copy() \
            for i in xrange(0, w, pw) for j in xrange(0, h, ph)]

def hist_similar(lh, rh):
    # 统计切分后每部分图片的相似度频率曲线
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)

def calc_similar(li, ri):
    # 计算两张图片的相似度
    return sum(hist_similar(l.histogram(), r.histogram()) for l, r in zip(split_image(li), split_image(ri))) / 16.0

def cmp_img(expect_img_file_path, export_img_file_path):
    u"""比较图片"""
    try:
        li = make_regalur_image(Image.open(expect_img_file_path))
        ri = make_regalur_image(Image.open(export_img_file_path))
        return calc_similar(li, ri)
    except Exception, e:
        raise e

def is_same_imgs(expect_img_file_path, export_img_file_path, ref="95"):
    u"""判断两张图片是否相同，默认大于等于95则认为两张图片相同"""
    try:
        if (cmp_img(expect_img_file_path, export_img_file_path) * 100) >= int(ref):
            return True
        else:
            return False
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
    input('xpath', "//input[@name='email']", username)
    input('xpath', "//input[@name='password']", password)
    click('id', "dologin")
    click('xpath', "//a[text()='继续登录']")
    sleep(3)
    # close_browser()
    assert_In(u"退出")

def addcontacts(name, mail, mobile, comment, is_set_star):
    u"""新建联系人"""
    click('xpath', "//div[@role='toolbar']//span[text()='新建联系人']")
    input('xpath', "//a[@title='编辑详细姓名']/preceding-sibling::div/input", name)
    input('xpath', "//*[@id='iaddress_MAIL_wrap']//input", mail)
    if is_set_star:
        click('xpath', "//span[text()='设为星标联系人']/preceding-sibling::span/b")
    input('xpath', "//*[@id='iaddress_TEL_wrap']//dd//input", mobile)
    input('xpath', "//textarea", comment)
    click('xpath', "//span[.='确 定']")

if __name__ == '__main__':
    open_browser("chrome")
    # browser_window_max()
    visit_url("http://www.baidu.com")
    # set_browser_window_position('200', '400')
    # set_browser_window_size('800', '600')
    # input('id', 'kw', "haha")
    # sleep("2")
    # send_Key('id', 'kw', 'enter')
    # sleep(2)
    # browser_back()
    # sleep(2)
    # browser_forward()
    # print get_select_options_texts('xpath', '//select')
    # print get_default_select_text('xpath', '//select')
    # print get_default_select_value('xpath', '//select')
    print get_window_title()
    print get_current_url()
    # print get_element_css_attr('id', 'kw','font-family')
    sleep(2)
    close_browser()