#encoding=utf-8
#encoding=utf-8
import time
from selenium.webdriver.support.ui import WebDriverWait

wait_time = 0.3

# 获取单个页面元素对象
def getElement(driver, locateType, locatorExpression):
    try:
        element = WebDriverWait(driver, 30).until\
            (lambda x: x.find_element(by = locateType, value = locatorExpression))
        time.sleep(wait_time)
        return element
    except Exception, e:
        raise e

# 获取多个相同页面元素对象，以list返回
def getElements(driver, locateType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 30).until\
            (lambda x:x.find_elements(by = locateType, value = locatorExpression))
        time.sleep(wait_time)
        return elements
    except Exception, e:
        raise e

if __name__ == '__main__':
    from selenium import webdriver
    # 进行单元测试
    driver = webdriver.Chrome(executable_path="d:\chromedriver.exe")
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver, "id", "kw")
    # 打印页面对象的标签名
    print searchBox.tag_name
    aList = getElements(driver, "tag name", "a")
    print len(aList)
    driver.quit()