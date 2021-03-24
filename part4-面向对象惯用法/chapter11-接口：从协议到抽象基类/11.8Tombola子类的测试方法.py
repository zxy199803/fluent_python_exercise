"""
利用常规类和抽象基类的API编写doctest

__subclasses__() 返回类的直接子类列表，不含虚拟子类
_abc_registry 只有抽象基类有这个数据属性，其值是一个WeakSet对象，即在抽象类注册的虚拟子类的弱引用
"""