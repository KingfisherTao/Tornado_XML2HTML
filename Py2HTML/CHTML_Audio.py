# coding=utf-8
# python 生成 Audio 的类
from Py2HTML.CHTML import CHTML


class CHTML_Audio(CHTML):
    """音频实现"""
    def __init__(self, h1Str: str, audioSrc: str):
        super(CHTML_Audio, self).__init__()

        # 定义音频 div
        _h1 = self.element('h1', h1=h1Str)
        _audio = self.element('audio', src=audioSrc)
        _div = self.element('div', id='', html_class='', div=f'{_h1}{_audio}')

        self.setBody(f'{self.NAV}{_div}')
