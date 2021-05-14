# coding=utf-8
# python 的 HTML 基类
from os.path import abspath, dirname
from traceback import print_exc
from Py2HTML.Py2HTML import Py2HTML
from Py2HTML.HTML_Template import HTML_BASE_TEMPLATE, HTML_NAV_LIST

# 这里是可选库导入的异常捕获，这个库是为了输出html时格式可读。此异常可忽略，不影响程序正常运行
try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

# 定义一些常量
TEMP_HREF = 0
TEMP_NAME = 1


class CHTML(Py2HTML):
    """定义一个 用 HTML_BASE_TEMPLATE 模板实现的HTML基础类 包含了顶部导航栏 此类可以看作是对 Py2HTML 的实现"""
    def __init__(self):
        super(CHTML, self).__init__()
        # 先读取 html 模板
        try:
            with open(HTML_BASE_TEMPLATE, "r", encoding="utf-8") as base:
                self.html = base.read()
        except Exception as error:
            print('CHTML.__init__ :', error)
            print_exc()

        # 定义顶部导航
        self.NAV = self.makeNav(HTML_NAV_LIST)

    def makeNav(self, navList: list) -> str:
        """基于 navList 构造导航栏"""
        _tempList = []
        for item in navList:
            _tempList.append(f'<li><a href={item[TEMP_HREF]}> {item[TEMP_NAME]} </a></li> \n')

        _nav = self.element('nav', nav=''.join(_tempList))
        _div = self.element('div', id='', html_class='', div=_nav)
        return _div

    def setTitle(self, title: str):
        self.html = self.html.replace('<title/>', title)

    def setBody(self, body: str):
        self.html = self.html.replace('<body/>', body)

    def get(self) -> str:
        return self.html

    def Write2HTML(self, filePath: str):
        with open(f'{dirname(dirname(abspath(__file__)))}{filePath}', 'w+', encoding='utf-8') as f:
            f.write(BeautifulSoup(self.html, 'html.parser').prettify()) if BeautifulSoup else f.write(self.html)
