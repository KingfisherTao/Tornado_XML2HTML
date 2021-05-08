# coding=utf-8
# python 的 HTML 基类
from os.path import abspath, dirname
from Py2HTML.Py2HTML import Py2HTML
from Py2HTML.HTML_Template import HTML_BASE_TEMPLATE, HTML_NAV_LIST

# 定义一些常量
_Temp_href = 0
_Temp_Name = 1


class CHTML(Py2HTML):
    """定义一个 用 HTML_BASE_TEMPLATE 模板实现的HTML基础类 包含了顶部导航栏 此类可以看作是对 Py2HTML 的实现"""
    def __init__(self):
        super(CHTML, self).__init__()
        # 先读取 html 模板
        try:
            with open(HTML_BASE_TEMPLATE, "r", encoding="utf-8") as base:
                self.html = base.read()
        except Exception as error:
            print(error)

        # 定义顶部导航
        _tempList = []
        for item in HTML_NAV_LIST:
            _tempList.append(f'<li><a href={item[_Temp_href]}> {item[_Temp_Name]} </a></li> \n')
        _nav = self.navTemp.safe_substitute(nav=''.join(_tempList))
        _divNav = self.divTemp.safe_substitute(div=_nav)

        self.NAV = _divNav

    def setTitle(self, title: str):
        self.html = self.html.replace('<title/>', title)

    def setBody(self, body: str):
        self.html = self.html.replace('<body/>', body)

    def get(self) -> str:
        return self.html

    def Write2HTML(self, filePath: str):
        with open(f'{dirname(dirname(abspath(__file__)))}{filePath}', 'w+', encoding='utf-8') as f:
            f.write(self.html)
