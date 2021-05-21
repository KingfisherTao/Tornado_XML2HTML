# coding=utf-8
try:
    from xml.etree.cElementTree import Element
except ImportError:
    from xml.etree.ElementTree import Element


def printElementByRootNode(node: Element):
    print(node.tag, node.text, node.attrib)
    for _sub in list(node):  # 以前的写法 是 node.getchildren() 但是貌似不用这么写了 ...
        printElementByRootNode(_sub)


def getElementsByTagName(node: Element, tagName: str, outList: list):
    for _sub in list(node):  # 以前的写法 是 node.getchildren() 但是貌似不用这么写了 ...
        if _sub.tag == tagName:
            outList.append(_sub)
        getElementsByTagName(_sub, tagName, outList)
