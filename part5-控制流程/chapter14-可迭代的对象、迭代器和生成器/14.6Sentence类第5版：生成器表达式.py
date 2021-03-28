"""
简单的生成器函数可以替换成生成器表达式。生成器表达式可以理解为列表推导的惰性版本，返回一个生成器按需惰性生成元素
列表推导：制造列表的工厂
生成器表达式：制造生成器的工厂

生成器表达式是语法糖
"""


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


res1 = [x * 3 for x in gen_AB()]  # 列表推导，迫切迭代了gen_AB()函数生成的生成器对象产出的元素
for i in res1:
    print('->',i)

res2 = (x*3 for x in gen_AB())  # 生成器表达式
print(res2)  # 生成器对象
for i in res2:
    print('->',i)


import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text  # 不再需要单词列表,self.text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))  # 没有yield,不再是生成器函数，使用生成器表达式构建生成器
