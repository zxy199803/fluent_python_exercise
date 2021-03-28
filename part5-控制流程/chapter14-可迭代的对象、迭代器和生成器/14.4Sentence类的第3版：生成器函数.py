"""
用生成器替代SentenceIterator类

只要Python函数的定义体中有yield关键字，该函数就是生成器函数，调用该函数会返回一个生成器对象
生成器函数是生成器工厂。
生成器函数会创建一个生成器对象，包装生成器函数的定义体
生成器函数，调用时构建了一个实现了迭代器接口的生成器对象

惰性实现：尽可能延后生成值，这样做能节省内存，或许还可以避免做无用的处理

"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):  # 不具有惰性
        self.text = text
        # 急迫地构建好了单词列表，将其绑定到self.words属性上
        self.words = RE_WORD.findall(text)  # 返回一个字符串列表，里面的元素是正则表达式的全部非重叠匹配。#

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # 生成器函数，调用时构建了一个实现了迭代器接口的生成器对象
        for word in self.words:  # 迭代self.words
            yield word  # 产出当前的word
        return


def gen_123():
    yield 1  # 只要函数包含关键字yield,该函数就是生成器函数
    yield 2
    yield 3


print(gen_123)  # 函数对象
print(gen_123())  # generator object，调用时返回生成器对象
for i in gen_123():  # 生成器是迭代器，会生成传给yield关键字的表达式的值
    print(i)
g = gen_123()
print(next(g), next(g), next(g))  # next会获取yield生成的下一个元素


# next(g)  # StopIteration

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


for c in gen_AB():
    print('->', c)
