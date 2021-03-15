"""
调用运算符（即()）
可调用对象
    用户定义的函数
        使用def或lambda创建
    内置函数
        使用C(CPython)实现的函数，如len,time.strftime
    内置方法
        使用C语言实现的方法，如dict.get
    方法
        在类的定义体中定义的函数
    类
        调用类时会运行类的__new__方法创建一个实例，然后运行__init__方法初始化实例，把实例返回给调用方
        python没有new运算符，所以调用类相当于调用函数
    类的实例
        如果类定义了__call__方法，它的实例可以作为函数调用
    生成器函数
        使用yield关键字的函数或方法。调用生成器函数返回的是生成器对象

使用callable()函数判断对象能否调用
"""
print([callable(obj) for obj in [abs, str, str(1), 13]])
