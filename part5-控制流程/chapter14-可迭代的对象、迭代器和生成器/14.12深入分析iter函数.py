"""
Python中迭代对象x时会调用iter(x)
iter函数还可以传入两个参数，使用常规的函数或任何可调用的对象创建迭代器。第一个参数必须是可调用的对象，用于不断调用产出各个值。第二个值是标记值，可调用对象返回这个值时触发迭代器抛出StopIteration异常
"""
from random import randint


def d6():
    return randint(1, 6)


d6_iter = iter(d6, 1)
for roll in d6_iter:
    print(roll)

# 逐行读取文件直到遇到空行或达到文件末尾
with open('my_data.txt') as fp:
    for line in iter(fp.readline,'\n'):
        process_line(line)
