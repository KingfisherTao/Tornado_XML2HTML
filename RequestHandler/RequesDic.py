# coding=utf-8
# 用来管理全部的 RequestHandler
from RequestHandler import *

TornadoHandler = \
    [
        (r'/index', IndexHandler.IndexHandler),
        (r'/pic', PictureHandler.PictureHandler),
        (r'/nav', NavHandler.NavHandler),
        (r'/t', TableHandler.TableHandler),
        (r'/video', VideoHandler.VideoHandler),
        (r'/audio', AudioHandler.AudioHandler)
    ]
