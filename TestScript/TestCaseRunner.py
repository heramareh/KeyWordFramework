#encoding=utf-8
from ProjectVar.var import *
from Util import Log
from Util.Excel import *
from Util.Log import *
from Action.Action import *
from Util.ParseSolution import get_solution, get_file_name_and_sheet_name

if __name__ == '__main__':
    for script in get_solution():
        print script
        file_name, sheet_name = get_file_name_and_sheet_name(script)
        pe = ParseExcel(os.path.join(test_data_path, file_name), sheet_name)
        for command in pe.get_commants():
            for id, command_line in enumerate(command):
                Log.info(command_line)
                start_time = time.time()
                try:
                    exec(command_line)
                    end_time = time.time()
                    # pe.write_cell_content(id+2, action_elapse_time_col_no, "%.2f" % (end_time - start_time))
                    # pe.write_cell_content(id + 2, action_result_col_no, u"成功")
                except:
                    end_time = time.time()
                    # pe.write_cell_content(id + 2, action_elapse_time_col_no, "%.2f" % (end_time - start_time))
                    # pe.write_cell_content(id + 2, action_result_col_no, u"失败")
                    Log.error(u"失败")
                    screen_shot()
                    Log.error(str(traceback.format_exc()))
                    raise
