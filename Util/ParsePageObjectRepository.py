#encoding=utf-8

import ConfigParser
import os
from ProjectVar.var import page_object_repository_path

class ParsePageObjectRepository(object):
    def __init__(self):
        self.configManage = ConfigParser.SafeConfigParser(allow_no_value=True)
        self.configManage.read(page_object_repository_path)

    def getSections(self):
        u"""获取所有节点"""
        return self.configManage.sections()

    def getOptions(self, section):
        u"""获取指定节点所有选项"""
        return self.configManage.options(section)

    def getItemsFromSection(self, section):
        u"""获取指定节点所有选项返回字典"""
        items = self.configManage.items(section)
        # print items
        # print dict(items)
        return dict(items)

    def getOptionValue(self, section, option):
        u"""获取指定节点下指定选项的值"""
        return self.configManage.get(section, option)

    def getBoolean(self, section, option):
        u"""获取指定节点下指定选项的布尔值"""
        return self.configManage.getboolean(section, option)

    def getInt(self, section, option):
        u"""获取指定节点下指定选项的整数"""
        return self.configManage.getint(section, option)

    def getFloat(self,section, option):
        u"""获取指定节点下指定选项的浮点数"""
        return self.configManage.getfloat(section, option)
if __name__ == '__main__':
    ppor = ParsePageObjectRepository()
    for section in ppor.getSections():
        print ppor.getOptions(section)
