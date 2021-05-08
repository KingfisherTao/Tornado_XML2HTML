# coding=utf-8
# python 生成 Index 的类
from Py2HTML.CHTML import CHTML


class CHTML_Index(CHTML):
    """欢迎页"""
    def __init__(self, body: str):
        super(CHTML_Index, self).__init__()

        # 定义首页 信息
        _h1 = self.h1Temp.safe_substitute(h1='Index')
        _div = self.divTemp.safe_substitute(div=f'{_h1}{body}')

        self.setBody(f'{self.NAV}{_div}')