# coding=utf-8
# python 生成 Table 的类
from Py2HTML.CHTML import CHTML


class CHTML_Table(CHTML):
    """table实现"""
    def __init__(self, h1Str: str, tdStr: str, table: str):
        super(CHTML_Table, self).__init__()

        # 定义表格 div
        _h1 = self.h1Temp.safe_substitute(h1=h1Str)
        _table = self.tableTemp.safe_substitute(border='1', style='width:100%; text-align:center;', colspan='4', td=tdStr,
                                                table=table)
        _a = self.aTemp.safe_substitute(href='nav', a='导航', target='', title='')
        _div = self.divTemp.safe_substitute(div=f'{_h1}{_table}{self.pTemp.safe_substitute(p="")}{self.brTemp}{_a}')

        self.setBody(f'{self.NAV}{_div}')
