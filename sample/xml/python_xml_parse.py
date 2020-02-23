# 转载:[数据解析之BeautifulSoup4解析库](https://www.jianshu.com/p/e7d9e2031430)
# coding:utf-8
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
</html>
"""
# 创建BeautifulSoup对象
# 使用BeautifulSoup进行解析
soup = BeautifulSoup(html, features="html.parser")
print(soup.prettify())
# print soup.head
print(soup.head)
# print soup.title
print(soup.title)
# print soup.a
print(soup.a)
# print soup.p
print(soup.p)
# 我们可以利用soup加标签名轻松地获取这些标签的内容，这些对象的类型是bs4.element.Tag。
# 它查找的是在所有内容中的第一个符合要求的标签。
# print type(soup.p) <class 'bs4.element.Tag'>
print(type(soup.title))

print("==================================================Tag==========================================================")
# 1.Tag: 对于Tag，它有两个重要的属性，分别是name和attrs
# print soup.head.name  对于其他内部标签，输出的值便为标签本身的名称
print(soup.head.name)
# print soup.p.attrs
# {'class': ['title'], 'name': 'dromouse'} 在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
print(soup.p.attrs)
# print soup.p['class']
print(soup.p['class'])
# 可以对这些属性和内容等等进行修改
soup.p['class'] = "newClass"
print(soup.p.attrs)

print("==================================================NavigableString==============================================")
# 2.NavigableString: 如果拿到标签后，还想获取标签中的内容。那么可以通过tag.string获取标签中的文字
# print soup.p.string
print(soup.p.string)
# <class 'bs4.element.NavigableString'>
print(type(soup.p.string))

print("==================================================BeautifulSoup==============================================")
# 3.BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作Tag对象,
# 它支持遍历文档树和搜索文档树中描述的大部分的方法.
# 因为BeautifulSoup对象并不是真正的HTML或XML的tag,所以它没有name和attribute属性.但有时查看它的 .name 属性是很方便的,
# 所以BeautifulSoup对象包含了一个值为 “[document]” 的特殊属性 .name
# print soup.name  soup 对象本身比较特殊，它的 name 即为 [document]
print(soup.name)

print("==================================================Comment==============================================")
# 4.Comment: Tag , NavigableString , BeautifulSoup 几乎覆盖了html和xml中的所有内容,
# 但是还有一些特殊对象.容易让人担心的内容是文档的注释部分。
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup2 = BeautifulSoup(markup, features="html.parser")
comment = soup2.b.string
print(comment)
print(type(comment))

print("==================================================遍历文档树==============================================")
# 5.遍历文档树
head_tag = soup.head
# 返回所有子节点的列表
print(head_tag.contents)
# 返回所有子节点的迭代器
for child in head_tag.children:
    print(child)

print("==================================================strings 和 stripped_strings===================================")
# 6.strings 和 stripped_strings
# 6.1.strings: 如果tag中包含多个字符串 [2] ,可以使用 .strings 来循环获取
print("==================================================strings===================================")
for string in soup.strings:
    print(repr(string))
# 6.2.stripped_strings: 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容
print("==================================================stripped_strings===================================")
for string in soup.stripped_strings:
    print(repr(string))

print("==================================================搜索文档树==================================")
# 7.搜索文档树
# 7.1. find和find_all方法：
# find方法是找到第一个满足条件的标签后就立即返回，只返回一个元素。
# find_all方法是把所有满足条件的标签都选到，然后返回回去。
# 最常用的用法是出入name以及attr参数找出符合要求的标签。
link = soup.find_all("a")
print(link)
link1 = soup.find("a")
print(link1)
link2 = soup.find_all("a", attrs={"id": "link2"})
print(link2)
link3 = soup.find_all("a", id='link3')
print(link3)
# 7.2.select方法
# 使用css选择器的语法，应该使用select方法
# 7.2.1.通过标签名查找
print(soup.select('a'))
# 7.2.2.通过类名查找：通过类名，则应该在类的前面加一个.
print(soup.select('.sister'))
# 7.2.3.通过id查找：通过id查找，应该在id的名字前面加一个＃号
print(soup.select('#link2'))
# 7.2.4.组合查找：组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的
print(soup.select("p #link3"))
# 7.2.5.通过属性查找：查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，
# 所以中间不能加空格，否则会无法匹配到。
print(soup.select('a[href="http://example.com/elsie"]'))
# 7.2.6.获取内容: 用 get_text() 方法来获取
for title in soup.select('title'):
    print(title.text)

# 7.3 过滤器
# 7.3.1 字符串
print("=============================过滤器：字符串=====================================")
# 查找文档中所有的<b>标签：
print(soup.find_all('b'))
# 7.3.2 正则表达式
print("=============================过滤器：正则表达式==================================")
# 找出所有以"b"开头的标签名称:
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# 7.3.3 列表
print("====过滤器：列表=================================================================")
# 找到文档中所有的<a>标签和<b>标签:
print(soup.find_all(['a', 'b']))
# 7.3.4 True
print("===============================过滤器：True======================================")
# 查找所有Tag,但是不会返回字符串节点
for tag in soup.find_all(True):
    print(tag.name)
# 7.3.5 函数
print("================================过滤器：函数======================================")

# 定义函数，检验当前元素，如果包含class属性却不包含id属性，那么将返回True
print("==函数1：检验当前元素，如果包含class属性却不包含id属性，那么将返回True=========")


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


print(soup.find_all(has_class_but_no_id))

# 找出href属性不符合指定正则表达式的<a>标签：
print("==函数2：找出href属性不符合指定正则表达式的<a>标签============================")


def not_lacie(href):
    return href and not re.compile("lacie").search(href)


print(soup.find_all(href=not_lacie))

# 过滤出前、后都有文字的标签
print("==函数3：过滤出前、后都有文字的标签============================")


def surrouned_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))


for tag in soup.find_all(surrouned_by_strings):
    print(tag.name)

print("==通过class_参数搜索有指定CSS类名的Tag============================")
# 通过class_参数搜索有指定CSS类名的Tag
print(soup.find_all(class_='sister', attrs={"id": "link1"}, href=re.compile('elsie$')))
# 当搜索到结果数量达到limit的限制时就停止搜索返回结果
print(soup.find_all("a", limit=2))
