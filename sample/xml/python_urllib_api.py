# coding:utf-8
# 转载自[Python3的urllib库基本使用](https://www.jianshu.com/p/0e7fc1b6b5cc)
# 转载自[json.dumps()和json.loads()](https://www.cnblogs.com/hjianhui/p/10387057.html)
from urllib import request
from urllib import parse
from urllib import error
import json

# 1.urllib.request请求模块
print("==================================1.urllib请求模块=====================================")
# 获取并打印百度的页面 GET请求
print("==================================获取并打印百度的页面GET请求=====================================")
some_url = "http://www.baidu.com"
response = request.urlopen(some_url)
# print(response.read().decode('utf-8'))
print('获取请求的url:', response.url)
# print('获取响应头信息:', response.headers)
print('获取状态码:', response.code)
print("==================================读取url内容，直接保存到本地=====================================")
# 读取url内容，直接保存到本地
# urllib.request.urlretrieve(url, './baidu.html')
# 获取图片
img_url = "http://img.sccnn.com/bimg/341/16243.jpg"
img_response = request.urlretrieve(img_url, './2020_love.jpg')
print('获取返回信息:', img_response)

# 2.urllib.parse: url解析模块
print("==================================2.urllib解析模块=====================================")
# 2.1 quote()编码: 按照RFC规定 URL中不能出现 空格 中文,只允许一部分 ASCII字符（数字字母和部分符号），
#     其他的字符（如汉字）是不符合 URL 标准的。所以，URL中使用其它字符就需要先进行编码。
code = parse.quote('北京')
print('quote()编码:', code)

# 2.2 unquote()解码: 其功能和quote相反, 对编码的内容进行解码。
city = parse.unquote('%E5%8C%97%E4%BA%AC')
print('unquote()解码:', city)

# 2.3 urlencode(): 对字典进行编码，把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
url = 'http://image.baidu.com/search/index?'
# http://image.baidu.com/search/index?tn=baiduimage&word=%E5%A5%B3%E6%9C%8B%E5%8F%8B

wd = '北京'
data = {
    'tn': 'baiduimage',
    'word': wd
}

# urlencode传入请求的数据对象 返回url编码后的字符串
query_string = parse.urlencode(data)
print('urlencode:%s%s' % (url, query_string))

# 3.请求头配置
print("==================================3.请求头配置=====================================")
# 3.1 配置请求头
# 谷歌浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}
# 创建请求对象
# 使用Request 传入 目标地址 请求参数 还有就是 字典形式的headers信息
request_obj = request.Request(url="http://www.baidu.com", headers=headers)
# urlopen的参数可以是简单的字符串 也可以是一个request请求对象
# 如果传入的是request请求对象则可以进行更高级的设置（比如设置headers）
response_obj = request.urlopen(request_obj)
print(response_obj.read().decode('utf-8'))

# 4.POST请求
print("==================================3.POST请求=====================================")
# 要请求的接口（手机端百度翻译的api接口，PC端的有验证 ）
fanyi_url = 'https://fanyi.baidu.com/sug'
form_data = {
    'kw': '你好'
}
# 如果没有请求头 headers 会被反爬
# 注意 传入的表单数据 需要是二进制数据， 所以我们需要对它进行编码
form_data_str = parse.urlencode(form_data)
# print(form_data_str)
# 把字符串变成二进制
bytes_data = form_data_str.encode()
# print(bytes_data)

request_obj = request.Request(fanyi_url, data=bytes_data, headers=headers)
response_obj = request.urlopen(request_obj)
# 二进制变字符串 decode 解码
# 要把Unicode符号 中的中文显示出来 需要使用 unicode_escape进行解码
result = response_obj.read().decode('utf-8')
dic = json.loads(result)
file = open('./fanyi.json', 'w', encoding='utf-8')
info = json.dump(dic, file, ensure_ascii=False, sort_keys=True, indent=4)
print("已写入文件")

# 4.URLError和HTTPError
print("==================================3.URLError和HTTPError=====================================")
# 一个不存在的连接
url = "https://www.baidu.com/"
req = request.Request(url)
try:
    response = request.urlopen(req)
    print("It's OK!")  # 正常
except error.HTTPError as error:  # HTTP错误
    print('HTTPError')
    print('ErrorCode: %s' % error.code)
except error.URLError as error:  # URL错误
    print(error.reason)
