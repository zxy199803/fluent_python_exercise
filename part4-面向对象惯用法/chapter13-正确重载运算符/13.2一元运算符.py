"""
一元运算符
    +(__pos__)
        一元取正运算符 x==+x
    -(__neg__)
    ~(__invert__)
        对整数按位取反，~x==-(x+1)
    abs()(__abs__)
    支持一元运算符只需实现相应的特殊方法，这些方法只有一个参数self

运算符的基本规则：始终返回一个新对象，不能修改self

算数运算符上下文的精度变化可能导致x不等于+x

__radd__是__add__的反射或反向版本,也称右向特殊方法
a+b a.__add__(b),b.__radd__(a)
"""
from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools


class Vector:
    typecpde = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.typecpde, components)  # array效率比List高，其背后存的是字节表述。受保护对象

    def __iter__(self):
        return iter(self._components)  # 返回可迭代对象

    def __repr__(self):  # 用于调试，绝对不能抛出异常，尽量输出有用内容让用户能识别目标对象
        components = reprlib.repr(self._components)  # reprlib.repr函数用于生成大型结构的安全表示形式，限制输出字符串的长度
        components = components[components.find('['):-1]  # 否则变成Vector(array('d', [3.0, 4.0,5.0))，
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecpde)]) + bytes(self._components)

    def __eq__(self, other):
        # return tuple(self) == tuple(other)  # 要构建两个元组，效率低

        # 提高比较效率
        # if len(self) != len(other):  # 一个输入耗尽，zip函数会停止生成值且不发出警告
        #     return False
        # for a, b in zip(self, other):
        #     if a != b:
        #         return False
        # return True

        # 更简单写法
        if isinstance(other, Vector):  # 做类型检查
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented  # Python会尝试调用其他方法比较

    def __hash__(self):
        # hashes = (hash(x) for x in self._components)
        hashes = map(hash, self._components)  # map函数是惰性的，会创建一个生成器，按需产出结果，因此可以节省内存
        return functools.reduce(operator.xor, hashes, 0)  # 0是初始值，防止序列为空

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):  # 不用传入self参数，通过cls传入类本身
        typecode = chr(octets[0])  # 第一个字节读取tpyecode
        memv = memoryview(octets[1:].cast(typecode))  # memoryview.cast 用不同的方式读写同一块内存数据，内容字节不会随意移动
        return cls(memv)

    # 可切片的序列
    def __len__(self):
        return len(self._components)

    # 此版本不能处理切片
    # def __getitem__(self, index):
    #     return self._components[index]

    # 能处理切片
    def __getitem__(self, index):
        cls = type(self)  # 返回对象的类型
        if isinstance(index, slice):  # 若index参数的值是slice对象
            return cls(self._components[index])  # 构造新的Vector类
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    # 动态存取属性
    def __setattr__(self, name, value):  # 改写了设置属性的逻辑
        cls = type(self)
        if len(name) == 1:  # 禁止为单个小写字幕属性赋值，防止与只读属性x,y,z,t混淆
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can not set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __getattr__(self, name):  # 仅当对象没有指定名称的属性时才会调用该方法
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    # 运算符重载
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)  # Vector实例是可迭代对象

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0)  # 生成(a,b)形式的元组，长度若不同，使用fillvalue填充。以此支持任何可迭代对象
            return Vector(a + b for a, b in pairs)  # 新的Vector实例
        except TypeError:  # 抛出异常就终止了运算符分派机制，最好将其捕获，返回NotImplemented，这样解释器就会尝试调用__radd__
            return NotImplemented

            # 由于类型不兼容而导致运算符特殊方法无法返回有效结果，应返回NotImplemented（特殊的单例值），NotImplementedError则是异常

    def __radd__(self, other):
        return self + other  # 直接委托给__add__

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):  # numbers.Real涵盖了所需的全部类型，还支持以后声明为numbers.Real抽象基类的真实子类或虚拟子类的数值类型
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar
