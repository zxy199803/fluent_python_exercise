"""
@contextmanager装饰器能减少创建上下文管理器的样板代码量，只需实现一个yield语句的生成器，生成想让__enter__方法返回的值
yield语句前面的所有代码在with块开始时（解释器调用__enter__方法时）执行，后面的在with块结束时（调用__exit__方法）执行

为了告诉解释器异常已经处理了，__exit__方法返回True,解释器会压制异常。如果__exit__方法没有显式返回一个值，解释器得到None,向上冒泡异常
使用@contextmanager时，默认行为相反，装饰器提供的__exit__方法假定发给生成器的异常都得到处理了，因此压制异常。不想让@contextmanager压制异常必须在被装饰函数中显式重新抛出异常
使用@contextmanager时要把yield放在try/finally(或with)语句中。因为我们永远不知道上下文管理器的用户会在with块中做什么


"""
import contextlib


# 无异常处理，抛出异常时函数中止，无法恢复成原来的方法
@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])  # 在闭包中访问original_write

    sys.stdout.write = reverse_write
    yield 'ABC'  # 产出一个值绑定到with语句中as子句的目标变量上
    # 控制权一旦跳出with块，继续执行yield之后的代码
    sys.stdout.write = original_write  # 这里恢复成原来的sys.stdout.write


with looking_glass() as what:
    print('cvb')
    print(what)

print(what)

@contextlib.contextmanager
def looking_glass1():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])  # 在闭包中访问original_write

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'ABC'
    except ZeroDivisionError:
        msg = 'Please Do NOT divide by zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)