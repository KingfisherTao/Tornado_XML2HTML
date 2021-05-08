# coding=utf-8
# python 生成 Picture 的类
from Py2HTML.CHTML import CHTML


class CHTML_Picture(CHTML):
    """图片实现"""
    def __init__(self, h1Str: str, imgSrc: str):
        super(CHTML_Picture, self).__init__()

        # 定义图片 div
        _h1 = self.h1Temp.safe_substitute(h1=h1Str)
        _img = self.imgTemp.safe_substitute(src=imgSrc)
        _div = self.divTemp.safe_substitute(div=f'{_h1}{_img}')

        self.setBody(f'{self.NAV}{_div}')
