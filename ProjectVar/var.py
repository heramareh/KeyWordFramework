#encoding=utf-8
import os

# 获取工程所在的目录的绝对路径
project_path = os.path.dirname(os.path.dirname(__file__))
page_object_repository_path = os.path.join(project_path, "Config", "PageObjectRepository.ini")
test_data_path = os.path.join(project_path, "TestData")
test_data_excel_path = os.path.join(test_data_path, u"126邮箱的测试用例.xlsx")
SolutionPath = os.path.join(project_path, "Solution")
# 浏览器驱动文件所在的绝对路径
ieDriverFilePath = os.path.join(project_path, "BroswerDriver", "IEDriverServer")
chromeDriverFilePath = os.path.join(project_path, "BroswerDriver", "chromedriver")
firefoxDriverFilePath = os.path.join(project_path, "BroswerDriver", "geckodriver")

# 截图绝对路径
CapturePicturePath = os.path.join(project_path, "ScreenPictures", "CapturePicture")
ErrorPicturePath = os.path.join(project_path, "ScreenPictures", "ErrorPicture")

# excel列名列号
actionNo = u'步骤序号'
actionName = u'动作'
locatorMethod = u'定位方式'
locatorExpression = u'定位表达式'
actionValue = u'操作值'
isRun = u'是否执行'
action_name_col_no=3
locator_method_col_no=4
locator_expression_col_no=5
action_value_col_no=6
action_elapse_time_col_no = 8
action_result_col_no = 9
action_excetion_info_col_no = 10
action_screen_info_col_no = 11

if __name__ == '__main__':
    print project_path
    print page_object_repository_path
    print test_data_excel_path