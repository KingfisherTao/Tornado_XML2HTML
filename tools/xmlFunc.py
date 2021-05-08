# coding=utf-8
def printElementByRootNode(node):
    print(node.tag, node.text, node.attrib)
    _children = node.getchildren()
    if _children is not None:
        for _sub in _children:
            printElementByRootNode(_sub)


def getElementsByTagName(node, tagName: str, outList: list):
    _children = node.getchildren()
    if _children is not None:
        for _sub in _children:
            if _sub.tag == tagName:
                outList.append(_sub)
            getElementsByTagName(_sub, tagName, outList)
