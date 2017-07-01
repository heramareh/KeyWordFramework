#encoding=utf-8
from ProjectVar.var import *
from Util.Excel import *
from Util.Log import *
from Action.Action import *

def get_all_solution():
    u"""读取TestData目录，获取所有excel以及excel所有的sheet名，
    以excel_name||sheet_name形式存放在列表中返回"""
    xlsx_files = []
    for root, dirs, files in os.walk(test_data_path):
        for file in files:
            if os.path.splitext(file)[1] == '.xlsx':
                xlsx_files.append(os.path.join(root, file))
    solution_all = []
    for xlsx_file in xlsx_files:
        pe = ParseExcel(xlsx_file)
        for sheet_name in pe.get_all_sheet_names():
            solution_all.append(os.path.split(xlsx_file)[1].decode('gbk') + "||" + sheet_name + '\n')
    return solution_all

def set_solution(file_name='solution_all.txt'):
    u"""设置执行脚本名文件"""
    with open(os.path.join(SolutionPath, file_name), 'w') as fp:
        fp.writelines(get_all_solution())

def get_solution():
    u"""获取solution文件中的执行脚本名，以#开头的脚本名除外"""
    contents = []
    with open(os.path.join(SolutionPath, 'solution.txt')) as fp:
        for each_line in fp.readlines():
            if not each_line.startswith("#"):
                contents.append(each_line.strip())
    return contents

def get_file_name_and_sheet_name(s):
    u"""用||拆分出来excel_name和sheet_name"""
    return s.split('||')[0].decode(), s.split('||')[1].decode()