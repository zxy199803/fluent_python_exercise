"""
装饰器在被装饰的函数定义后立即运行
被装饰的函数只有在明确调用时运行
这是导入时和运行时的区别

实际上装饰器通常在一个模块中定义，应用到其他模块函数上
大多数装饰器会在内部定义一个函数然后将其返回
"""
registry = []  # registry 注册

# 调用register时，传给它的参数是被装饰的函数
def register(func):
    print('running register(%s)' % func)  # 显示被装饰的函数
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')  # register在模块中的其他函数之前运行了两次
    print('registry ->', registry)  # 加载模块后，registry中有两个被装饰函数的引用
    f1()
    f2()
    f3()


if __name__ == '__main__':  # 只有把本代码当做脚本运行时才调用main()
    main()
