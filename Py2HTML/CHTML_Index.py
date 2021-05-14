# coding=utf-8
# python 生成 Index 的类
from Py2HTML.CHTML import CHTML


class CHTML_Index(CHTML):
    """欢迎页"""
    def __init__(self, body: str):
        super(CHTML_Index, self).__init__()

        # 定义首页 信息
        _h1 = self.element('h1', h1='Index')
        _div = self.element('div', id='', html_class='', div=f'{_h1}{body}')

        self.setBody(f'{self.NAV}{_div}')
