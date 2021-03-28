"""
实际Iterator接口时考虑了惰性，next()一次生成一个元素。
惰性求值(lazy evaluation),及早求值(eager evaluation)

re.finditer 是 re.findall的惰性版本，返回生成器而不是列表
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text  # 不再需要单词列表,self.text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # 只有需要的时候才生成下一个单词
        for match in RE_WORD.finditer(self.text):  # 构建迭代器，包含self.text中匹配RE_WORD的单词，产出MatchObject实例
            yield match.group()  # match.group()方法从MatchObject实例提取匹配正则表达式的具体文本


class Bus:
    def __init__(self, passengers):
        self.passengers = passengers  # self.passengers与passengers指向的对象相同

    def show(self):
        for p in self.passengers:
            print(p)


passengers = [1, 2]
b = Bus(passengers)
b.show()

passengers.append(3)
b.show()
