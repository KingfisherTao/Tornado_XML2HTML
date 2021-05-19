# coding=utf-8
from abc import ABC
from tornado.web import RequestHandler
from Py2HTML.CHTML_Table import CHTML_Table
try:
    from xml.etree.cElementTree import parse
except ImportError:
    from xml.etree.ElementTree import parse
from tools import *


# t
class TableHandler(RequestHandler, ABC):
    def get(self):
        # 从xml读取数据
        _xmlFile = parse(r'./data/data.xml')
        _root = _xmlFile.getroot()
        printElementByRootNode(_root)
        _myList = []
        getElementsByTagName(_root, 'student', _myList)
        _student_tr = []
        for _s in _myList:
            _student_tr.append(f'<td>{_s.get("id")}</td>')
            for _ss in _s:
                _student_tr.append(f'<td>{_ss.text}</td>')

        _student_trs = f'<tr>{"".join(_student_tr)}</tr>'

        _html = CHTML_Table('./data/data.xml', '人员信息', _student_trs)
        _html.setTitle('人员信息')

        self.write(_html.get())
