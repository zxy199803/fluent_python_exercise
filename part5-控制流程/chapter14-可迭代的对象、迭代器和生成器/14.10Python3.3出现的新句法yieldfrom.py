"""
yield from 把不同生成器结合在一起使用
"""
def my_chain(*iteralbes):
    for it in iteralbes:
        for i in it:
            yield i

s = 'ABC'
t = tuple(range(3))
print(list(my_chain(s,t)))

def chain(*iteralbes):
    for i in iteralbes:
        yield from i  # 代替了内层的for循环