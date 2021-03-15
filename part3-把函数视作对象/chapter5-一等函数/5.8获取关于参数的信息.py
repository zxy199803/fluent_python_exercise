"""
HTTP微框架Bobo
函数对象有__defaults__属性，值是元组，保存着定位参数和关键字参数的默认值
仅限关键字参数的默认值在__kwdefaults__属性中
参数的名称在__code__属性中，它的值是一个code对象的引用

inspect模块
kind属性的值是_ParameterKind类中的五个之一：
    POSITIONAL_OR_KEYWORD
        可以通过定位参数和关键字参数传入的形参
    VAR_POSITIONAL
        定位参数元组(如*v)
    VAR_KEYWORD
        关键字参数字典(如**d)
    KEYWORD_ONLY
        仅限关键字参数(位于定位参数元组后)
    POSITIONAL_ONLY
        仅限定位参数，Python声明函数的句法不支持，有些C语言实现且不接受关键字参数的函数(如divmod)支持

inspect,Signature 对象有个bind方法，把任意个参数绑定到签名中的形参上，所用规则与实参到形参的匹配方式一样。框架可以使用这个方法在真正调用函数前验证参数
"""
# Bobo知道hello需要person参数，并从HTTP请求中获取它
import bobo


@bobo.query('/')  # bobo.query装饰器把一个普通函数与框架的请求处理机制集成起来了
def hello(person):
    return 'Hello %s!' % person


def clip(text, *v, max_len=80, **d):
    """
    在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


print(clip.__defaults__)  # 参数的默认值通过它们在__defaults__元组中的位置确定，从后向前扫描把参数和默认值对应起来
print(clip.__code__)
print(clip.__code__.co_varnames)  # 参数名称、函数定义体中创建的局部变量
print(clip.__code__.co_argcount)  # 参数名称是前N个字符串，N由__code__.co_argcount决定

from inspect import signature

sig = signature(clip)  # 有parameters属性，是有序映射，把参数名和inspect.Parameter对象对应起来。
print(str(sig))
for name, parm in sig.parameters.items():
    print(parm.kind, ':', name, '=', parm.default)  # inspect._empty表示没有默认值

import inspect


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


sig_tag = inspect.signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig_tag.bind(**my_tag)  # 把一个字典参数传给.bind()方法
for name, value in bound_args.arguments.items():  # bound_args.arguments是一个OrderedDict 对象。迭代显示参数的名称和值
    print(name, '=', value)
