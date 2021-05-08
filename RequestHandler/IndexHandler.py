# coding=utf-8
from abc import ABC
from tornado.web import RequestHandler
from Py2HTML.CHTML_Index import CHTML_Index


# index
class IndexHandler(RequestHandler, ABC):
    def get(self):
        _html = CHTML_Index('Hello World <br/> This My Tornado Demo <br/>')
        _html.setTitle('Index')

        self.write(_html.get())
