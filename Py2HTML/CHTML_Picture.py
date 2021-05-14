# coding=utf-8
# python 生成 Picture 的类
from Py2HTML.CHTML import CHTML


class CHTML_Picture(CHTML):
    """图片实现"""
    def __init__(self, h1Str: str, imgSrc: str):
        super(CHTML_Picture, self).__init__()

        # 定义图片 div
        _h1 = self.element('h1', h1=h1Str)
        _img = self.element('img', id='', html_class='', src=imgSrc)
        _div = self.element('div', id='', html_class='', div=f'{_h1}{_img}')

        self.setBody(f'{self.NAV}{_div}')
