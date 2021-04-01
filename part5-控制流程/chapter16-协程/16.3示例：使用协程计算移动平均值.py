def averager0():
    total = 0.0
    count = 0
    average = None
    while True:  # 只要调用方不断发值给协程，就一直接收，生成结果。仅当调用方在协程上调用.close()方法，或者没有对这个协程的引用而被垃圾回收时协程才终止
        term = yield average  # 用于暂停执行协程，把结果发给调用方，接收调用方后面发给协程的值
        total += term
        count += 1
        average = total / count
# 使用协程后，total和count声明为局部变量即可，无需使用示例属性或闭包多次调用之间保持上下文

coro_avg = averager0()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(20))
