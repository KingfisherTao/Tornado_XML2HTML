# coding=utf-8
try:
    from xml.etree.cElementTree import Element
except ImportError:
    from xml.etree.ElementTree import Element


def printElementByRootNode(node: Element):
    print(node.tag, node.text, node.attrib)
    for _sub in list(node):  # ��ǰ��д�� �� node.getchildren() ����ò�Ʋ�����ôд�� ...
        printElementByRootNode(_sub)


def getElementsByTagName(node: Element, tagName: str, outList: list):
    for _sub in list(node):  # ��ǰ��д�� �� node.getchildren() ����ò�Ʋ�����ôд�� ...
        if _sub.tag == tagName:
            outList.append(_sub)
        getElementsByTagName(_sub, tagName, outList)
