"""
参数化装饰器通常会把被装饰的函数替换掉，且结构上需要多一层嵌套
"""
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

# 有两层函数嵌套
def clock(fmt=DEFAULT_FMT):  # 参数化装饰器工厂函数
    def decorate(func):  # 真正的装饰器
        def clocked(*_args):  # 包装被装饰的函数
            t0 = time.time()
            _result = func(*_args)  # 被装饰的函数返回的真正结果
            elapsed = time.time() - t0
            name = func.__name__
            args = ' .'.join(repr(_args) for arg in _args)
            result = repr(_result)  # _result的字符串形式，用于显示
            print(fmt.format(**locals()))
            return _result  # clocked会取代被装饰的函数，因此它应返回被装饰函数的返回的值

        return clocked

    return decorate


if __name__ == '__main__':
    @clock('{name}:{elapsed}s')
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)
