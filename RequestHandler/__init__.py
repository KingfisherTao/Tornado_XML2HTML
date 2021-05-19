# coding=utf-8
from RequestHandler.IndexHandler import IndexHandler
from RequestHandler.VideoHandler import VideoHandler
from RequestHandler.TableHandler import TableHandler
from RequestHandler.PictureHandler import PictureHandler
from RequestHandler.NavHandler import NavHandler
from RequestHandler.AudioHandler import AudioHandler

TornadoHandler = \
    [
        (r'/index', IndexHandler),
        (r'/pic', PictureHandler),
        (r'/nav', NavHandler),
        (r'/t', TableHandler),
        (r'/video', VideoHandler),
        (r'/audio', AudioHandler)
    ]

__all__ = ['TornadoHandler']
