# coding=utf-8
from abc import ABC
from tornado.web import RequestHandler
from Py2HTML.CHTML_Picture import CHTML_Picture


# pic
class PictureHandler(RequestHandler, ABC):
    def get(self):
        _html = CHTML_Picture('图片', '/static/images/imgtest_1.jpg')
        _html.setTitle('图片')

        self.write(_html.get())
