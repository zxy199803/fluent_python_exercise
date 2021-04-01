"""
协程可以处在四个状态中的一个，当前状态用inspect.getgeneratorstate()函数确定
    ‘GEN_CREATED’ 等待开始执行
    'GEN_RUNNING' 解释器正在执行，只有多线程应用中才能看到这个状态
    'GEN_SUSPENDED' 在yield表达式处暂停
    'GEN_CLOSED' 执行结束

send方法的参数会成为暂定的yield表达式的值，仅当协程处于暂停状态时才能调用send方法
始终要用next()或send(None)激活协程  （预激(prime)协程）

=右边的代码在赋值之前执行
"""


def simple_coroutine():
    print('-> coroutine started')
    x = yield  # yield在表达式中使用，如果协程只需从用户那里接收数据，那么产出值是None
    print('-> coroutine received:', x)


# my_coro = simple_coroutine()
# print(my_coro)  # 调用函数得到生成器对象
# next(my_coro)  # 首先调用next函数，因为生成器还没启动，没在yield语句暂定，一开始无法发送数据
# my_coro.send(45)


def simple_coro2(a):
    print('-> Started:a=', a)
    b = yield a  # 执行yield a,产出数字
    print('-> Received:b=', b)
    c = yield a + b
    print('-> Received:c=', c)

my_coro2 = simple_coro2(14)
from inspect import getgeneratorstate

next(my_coro2)

my_coro2.send(28)

my_coro2.send(99)
