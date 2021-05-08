# coding=utf-8
from abc import ABC
from tornado.web import RequestHandler
from Py2HTML.CHTML_Audio import CHTML_Audio


# audio
class AudioHandler(RequestHandler, ABC):
    def get(self):
        _html = CHTML_Audio('音频', '/static/audio/test.mp3')
        _html.setTitle('音频')

        self.write(_html.get())
