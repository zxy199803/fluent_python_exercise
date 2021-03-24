"""
每个抽象基类都依赖abc.ABC类，除非定义新的抽象基类，否则不用导入

collections.abc模块中的抽象基类
    定义了16个抽象基类
    Iterable、Container、Sized
        各个集合应继承这三个抽象基类，或至少实现兼容协议
        Iterable通过__iter__方法支持迭代
        Container通过__contains__方法支持in运算符
        Sized通过__len__方法支持len()函数

    Sequence、Mapping、Set
        是主要的不可变集合类型，各自都有可变子类

    MappingView
        映射方法.items()、.keys()、.values()返回的对象分别是ItemsView、KeysView、ValuesView的实例

    Callable、Hashable
        为内置函数isinstance提供支持，以一种安全的方式判断对象能不能调用或散列
        测试对象是否可散列:isinstance(my_obj,Hashable)

    Iterator
        是Iterable的子类

numbers包定义的数字塔（各个抽象基类的层次结构是线性的）
    Number
    Complex
    Real
    Rational
    Integral

    检查一个数是不是整数：isinstance(x,numbers.Integral)，这样代码能接受int,bool（int的子类）
"""