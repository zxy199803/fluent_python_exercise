"""
Python 极其灵活的参数处理机制
仅限关键字参数是Python3新增特性，如例子中cls参数只能通过关键字参数指定，不会捕获未命名的定位参数
定义函数时若想指定仅限关键字参数要放到前面有*的参数后面
不想支持数量不定的定位参数，但支持仅限关键字参数，在签名中放一个*
"""


# tag函数生成HTML标签
def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


print(tag('br'))  # 传入单个定位参数，生成一个指定名称的空标签
print(tag('p', 'hello'))  # 第一个参数后的任意个参数会被*content捕获，存入一个元组
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))  # tag函数签名中没有明确指定名称的关键字参数会被**attrs捕获，存入一个字典
print(tag('p', 'hello', 'world', cls='sidebar'))  # cls参数只能作为关键字参数传入
print(tag(content='testing', name='img'))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))  # 字典中的所有元素作为单个参数传入，同名键绑定对应的具名参数上，其余被**attrs捕获


def f(a, *, b):
    return a, b


# print(f(1,b=3,2))  # SyntaxError: positional argument follows keyword argument
# print(f(1,2,b=3))  # TypeError: f() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given

