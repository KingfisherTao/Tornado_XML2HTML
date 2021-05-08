# coding=utf-8
# python 的 html 模板基类
from abc import ABCMeta, abstractmethod
from string import Template as T
from Py2HTML.HTML_Template import *


class Py2HTML(metaclass=ABCMeta):
    """定义一个 所有用 python 生成 HTML 的基类"""

    def __init__(self):
        """
        初始化函数，主要是为了初始化 HTML_Template 中定义的 HTML 模板
        (以后这些模板还可根据需要继续添加)
        """
        self.scriptTemp = T(HTML_SCRIPT)    # 脚本模板
        self.tableTemp = T(HTML_TABLE)      # 表格模板
        self.audioTemp = T(HTML_AUDIO)      # 音频模板
        self.videoTemp = T(HTML_VIDEO)      # 视频模板
        self.nobrTemp = T(HTML_NOBR)        # 无换行模板
        self.spanTemp = T(HTML_SPAN)        # span模板
        self.bodyTemp = T(HTML_BODY)        # body模板
        self.divTemp = T(HTML_DIV)          # div模板
        self.imgTemp = T(HTML_IMG)          # 图片模板
        self.navTemp = T(HTML_NAV)          # 导航模板
        self.h1Temp = T(HTML_H1)            # h1模板
        self.brTemp = T(HTML_BR)            # 换行符模板
        self.aTemp = T(HTML_A)              # 链接模板
        self.pTemp = T(HTML_P)              # 段落模板

        # 每个 Py2HTML 的基类都需要生成一个 html 字符串 用来写入文件或者直接交给 Tornado 进行路由
        self.html = None

    @abstractmethod
    def setTitle(self, title: str):
        """设置 Title (抽象方法必须由子类实现)"""
        raise AttributeError('Subclasses must implement this method')

    @abstractmethod
    def setBody(self, body: str):
        """设置 body (抽象方法必须由子类实现)"""
        raise AttributeError('Subclasses must implement this method')

    @abstractmethod
    def get(self) -> str:
        """提供给外部调用 (抽象方法必须由子类实现)"""
        raise AttributeError('Subclasses must implement this method')

    @abstractmethod
    def Write2HTML(self, filePath: str):
        """将 self.html 写入 filePath 保存成 html文件 (抽象方法必须由子类实现)"""
        raise AttributeError('Subclasses must implement this method')