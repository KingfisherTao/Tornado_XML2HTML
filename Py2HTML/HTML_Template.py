# coding=utf-8
# 此文件定义了很多 HTML 中会用到的字符串常量

HTML_BASE_TEMPLATE = './static/template/base.html'

HTML_BODY = """
<body bgcolor="${bgcolor}" leftmargin="${leftmargin}" topmargin="${topmargin}" marginwidth="${marginwidth}" 
marginheight="${marginheight}"${onmousemove}${onload}> 
${body} 
</body>
"""

HTML_SCRIPT = """
    <script> ${script}   </script>
"""

HTML_DIV = """
    <div ${id} ${html_class}> ${div} </div>
"""

HTML_NOBR = """
    <nobr> ${nobr}   </nobr>
"""

HTML_H1 = """
<h1> ${h1} </h1>
"""
HTML_A = """
<a href="${href}"${onclick} ${ondblclick} ${target} ${title} ${onmousemove}> ${a}  </a>
"""

HTML_P = """
<p> ${p} </p>
"""

HTML_TABLE = """
<table border="${border}" style="${style}">
    <tr>
        <td colspan=${colspan}> ${td} </td>
    </tr>
    ${table}
</table>
"""

# 在这里定义多个 list 用来做导航列表中的对象 元素【href，titile】
HTML_NAV_LIST = [['index', 'Index'], ['pic', '图片'], ['video', '视频'], ['audio', '音频'], ['t', '表格']]

HTML_NAV = """
<ul class="nav nav-tabs">
    ${nav}
</ul>
"""

HTML_VIDEO = """
<video width="${width}" height="${height}" controls autoplay>
    <source src=${src}>
</video>
"""

HTML_IMG = """
    <img ${id}src="${src}" class="${html_class}">
"""


HTML_SPAN = """
    <span id="${id}" class="${html_class}">${span}</span>
"""

HTML_AUDIO = """
<audio src=${src} controls></audio>
"""

HTML_BR = """
<br/>
"""

