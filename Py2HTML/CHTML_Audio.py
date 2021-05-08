# coding=utf-8
# python 生成 Audio 的类
from Py2HTML.CHTML import CHTML


class CHTML_Audio(CHTML):
    """音频实现"""
    def __init__(self, h1Str: str, audioSrc: str):
        super(CHTML_Audio, self).__init__()

        # 定义音频 div
        _h1 = self.h1Temp.safe_substitute(h1=h1Str)
        _audio = self.audioTemp.safe_substitute(src=audioSrc)
        _div = self.divTemp.safe_substitute(div=f'{_h1}{_audio}')

        self.setBody(f'{self.NAV}{_div}')
