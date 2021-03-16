"""
装饰器是可调用的对象，其参数是另一个函数
装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象

装饰器能把被装饰的函数替换成其他函数
装饰器在加载模块时立即执行

可以在函数中定义函数，其在函数之外是不能访问的（嵌套的函数）
函数也能返回函数
"""


def deco(func):
    def inner():
        print('running inner()')

    return inner  # 返回inner函数对象


@deco
def target():
    print('running target()')


target()  # 调用被装饰的target其实会运行inner
print(target)