"""
把register当装饰器

把register当函数，用于注册其他地方定义的类。如collections,abc中把内置类型tuple,str注册为Sequence的虚拟子类
Sequence.register(tuple)
"""
