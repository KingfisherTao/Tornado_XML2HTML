# coding=utf-8
from abc import ABC
from tornado.web import RequestHandler
from Py2HTML.CHTML_Video import CHTML_Video


# video
class VideoHandler(RequestHandler, ABC):
    def get(self):
        _html = CHTML_Video('视频', '/static/video/test.mp4', '800', '600')
        _html.setTitle('视频')

        self.write(_html.get())
