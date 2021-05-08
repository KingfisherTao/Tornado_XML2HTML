# coding=utf-8
from abc import ABC
from tornado.web import RequestHandler
from Py2HTML.CHTML_NAV import CHTML_NAV


# nav
class NavHandler(RequestHandler, ABC):
    def get(self):
        _html = CHTML_NAV()
        _html.setTitle('导航页')

        self.write(_html.get())
