#encoding=utf-8

import logging
import logging.config
import os
import ProjectVar.var as var

# 读取日志的配置文件
logging.config.fileConfig(os.path.join(var.project_path, 'Config', 'Logger.conf'))
#选择一个日志格式
logger = logging.getLogger("example01") # example01

def debug(message):
    u"""打印debug级别的信息"""
    return logger.debug(message)

def info(message):
    u"""打印info级别的信息"""
    return logger.info(message)

def warning(message):
    u"""打印warning级别的信息"""
    return logger.warning(message)

def error(message):
    u"""打印error级别的信息"""
    return logger.error(message)

if __name__ == '__main__':
    print os.path.join(var.project_path, 'Config', 'Logger.conf')
    debug("debug information")
    info("info information")
    warning("warning information")
    error("error information")
