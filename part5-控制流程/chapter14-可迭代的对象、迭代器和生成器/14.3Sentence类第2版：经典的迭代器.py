"""
通过这一版明确可迭代集合和迭代器对象之间的关系。展示了典型的迭代器模式

根据协议，__iter__方法实例化并返回一个迭代器

迭代器实现__next__和__iter__方法能让迭代器通过issubclass(SentenceInterator,abc.Iterator)测试

把Sentence变成迭代器：坏主意
    可迭代对象
        有__iter__方法，每次实例化一个新的迭代器
    迭代器
        实现__next__方法返回单个元素
        实现__iter__方法返回迭代器本身
    迭代器可迭代，可迭代的对象不是迭代器

迭代器模式用来
    访问一个聚合对象的内容而无需暴露它的内部表示
    支持对聚合对象的多种遍历。
    为遍历不同的聚合结构提供一个统一的接口（即支持多态迭代）

为支持多种遍历，必须从同一个可迭代的实例中获取多个独立的迭代器，各个迭代器要能维护自身的内部状态，为此需要每次调用iter()都能新建一个独立的迭代器

可迭代对像一定不能是自身的迭代器，可迭代对象必须实现__iter__方法，不能实现__next__方法
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # 返回一个字符串列表，里面的元素是正则表达式的全部非重叠匹配

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)  # 实例化并返回一个迭代器


class SentenceIterator:
    def __init__(self, words):
        self.words = words  # SentenceIterator实例引用单词列表
        self.index = 0  # 用于确定下一个要获取的单词

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self
