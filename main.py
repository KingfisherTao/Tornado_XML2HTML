# coding=utf-8
from os import path
from tornado import ioloop
from tornado.web import Application, StaticFileHandler
from tornado.options import define, options
from RequestHandler.RequesDic import TornadoHandler

if __name__ == '__main__':
    define('port', default='8000', type=int, help="listening port")
    options.parse_command_line()

    # 创建路由 handler
    _handlers = [
        # 网页左上角的icon
        (r'favicon.ico', StaticFileHandler, dict(url=path.join(path.dirname(__file__), '/static/icons/FF7.ico'),
                                                 permanent=False)),
    ]

    # 添加需要路由的页面
    for item in TornadoHandler:
        _handlers.append(item)

    # setting
    _settings = {
        'debug': False,
        'static_path': 'static',
        'template_path': 'template',
        'static_url_prefix': '/static/'
    }

    # 初始化 app 并启动
    _app = Application(handlers=_handlers, **_settings)
    _app.listen(options.port)
    print(f'starting tornado on port {options.port}')
    ioloop.IOLoop.current().start()
