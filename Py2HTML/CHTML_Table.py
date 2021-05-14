# coding=utf-8
# python 生成 Table 的类
from Py2HTML.CHTML import CHTML


class CHTML_Table(CHTML):
    """table实现"""

    def __init__(self, h1Str: str, tdStr: str, table: str):
        super(CHTML_Table, self).__init__()

        # 定义表格 div
        _h1 = self.element('h1', h1=h1Str)
        _table = self.element('table', border='1', style='width:100%; text-align:center;', colspan='4', td=tdStr,
                              table=table)
        _a = self.element('a', href='nav', a='导航', target='', title='', onclick='', ondblclick='', onmousemove='')
        _div = self.element('div', id='', html_class='',
                            div=f'{_h1}{_table}{self.element("p", p="")}{self.element("br")}{_a}')

        self.setBody(f'{self.NAV}{_div}')
