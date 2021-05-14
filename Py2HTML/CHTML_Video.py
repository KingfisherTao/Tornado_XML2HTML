# coding=utf-8
# python 生成 Video 的类
from Py2HTML.CHTML import CHTML


class CHTML_Video(CHTML):
    """视频实现"""
    def __init__(self, h1Str: str, videoSrc: str, width: str, height: str):
        super(CHTML_Video, self).__init__()

        # 定义视频 div
        _h1 = self.element('h1', h1=h1Str)
        _video = self.element('video', src=videoSrc, width=width, height=height)
        _div = self.element('div', id='', html_class='', div=f'{_h1}{_video}')

        self.setBody(f'{self.NAV}{_div}')
