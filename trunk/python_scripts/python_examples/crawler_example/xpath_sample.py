from lxml import etree

html_doc = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<ul class="list" id="list-1">
<li class="element"><a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list two" id="list-2">
<li class="element"><a href="http://example.com/tillie" class="parent" id="link3">Tillie</a>evan</li>
<li class="element">jane</li>
<li class="element">summer</li>
</ul>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="child" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="parent" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">End...</p>
</body>
</html>
"""


def parse():
    """常用表达式规则：
    nodename    选择此节点的所有子节点
    /           从当前节点选取直接子节点
    //          从当前节点选取子孙节点
    .           选取当前节点
    ..          选取当前节点的父节点
    @           选取属性
    *           选取所有信息
    """
    # 初始化对象
    html = etree.HTML(html_doc)  # # html文本初始化
    # html = etree.parse(./example.html, etree.HTMLParser())  # html文件初始化

    # 补全HTML代码
    print(etree.tostring(html).decode('utf-8'))

    # 获取所有节点
    print(html.xpath('//*'))  # 获取所有节点，返回一个列表
    print(html.xpath('//li'))  # 获取所有的li节点，返回一个列表
    # 获取父·子节点
    print(html.xpath('//a[@class="parent"]/..'))  # 获取所有a节点内class等于'parent'的直接父节点，返回一个列表
    print(html.xpath('//a[@class="parent"]/parent::*'))  # 用法同上
    print(html.xpath('//ul/li'))  # 获取所有ul节点下的直接li节点，返回一个列表
    print(html.xpath('//ul//a'))  # 获取所有ul节点下的所有子孙a节点，返回一个列表

    # 文本获取
    print(html.xpath('//a[@class="parent"]/text()'))  # 获取所有a节点内class等于'parent'的文本，返回一个列表
    # 属性获取
    print(html.xpath('//ul/@class'))  # 获取所有ul节点内的class值，返回一个列表

    # 属性匹配
    print(html.xpath('//ul[@class="list"]'))  # 获取所有class等于'list'的ul节点，返回一个列表
    # 属性多值匹配
    print(html.xpath('//ul[contains(@class, "two")]'))  # 获取所有class包含'two'的ul节点，返回一个列表
    # 多属性匹配
    print(html.xpath('//ul[contains(@class, "two") and @id="list-2"]'))  # 满足上面的情况再加上id等于'list-2'，返回一个列表


if __name__ == '__main__':
    parse()
