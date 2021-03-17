"""
解析源码中的装饰器时，Python把被装饰的函数作为第一个参数传递给装饰器函数
让装饰器接受其他参数：
    创建一个装饰器工厂函数，把参数传给它，返回一个装饰器再把它应用到要装饰的函数上


"""
registry = set() # set对象添加和删除函数的速度更快


def register0(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


def register(active=True):  # 装饰器工厂函数
    def decorate(func):  # 这个内部函数是真正的装饰器
        print('running register(active=%s) ->decorate(%s)'%(active,func))
        if active:  # active参数从闭包中获取
            registry.add(func)
        else:
            registry.discard(func)  # 删除
        return func
    return decorate


@register()  # 工厂函数必须作为函数调用，即要返回真正的装饰器decorate
def f1():
    print('running f1()')


print('running main()')
print('registry ->', registry)
f1()

# 不使用@句法，像常规函数那样使用register
register(active=False)(f1)