# coding=utf-8
# python 生成 NAV 的类
from Py2HTML.CHTML import CHTML


class CHTML_NAV(CHTML):
    """导航页，因为跟基类的导航数据一致故没什么好修改的"""
    def __init__(self):
        super(CHTML_NAV, self).__init__()
        self.setBody(self.NAV)
