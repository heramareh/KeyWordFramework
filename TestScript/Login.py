#encoding=utf-8
from ProjectVar.var import *
from Util.Excel import *
from Util.Log import *
from Action.Action import *

pe = ParseExcel(test_data_excel_path)
for sheet_name in pe.get_all_sheet_names():
    print sheet_name
    pe = ParseExcel(test_data_excel_path, sheet_name)
    for command in pe.get_commants():
        for id, command_line in enumerate(command):
            print command_line
            start_time = time.time()
            try:
                exec(command_line)
                end_time = time.time()
                pe.write_cell_content(id+2, action_elapse_time_col_no, "%.2f" % (end_time - start_time))
                pe.write_cell_content(id + 2, action_result_col_no, u"成功")
            except:
                end_time = time.time()
                pe.write_cell_content(id + 2, action_elapse_time_col_no, "%.2f" % (end_time - start_time))
                pe.write_cell_content(id + 2, action_result_col_no, u"失败")
                pe.write_cell_content(id + 2, action_excetion_info_col_no, screen_shot())
                pe.write_cell_content(id + 2, action_screen_info_col_no, traceback.format_exc())