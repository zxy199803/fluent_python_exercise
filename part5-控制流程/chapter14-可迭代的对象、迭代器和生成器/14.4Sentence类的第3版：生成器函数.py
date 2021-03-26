"""
用生成器替代SentenceIterator类

只要Python函数的定义体中有yield关键字，该函数就是生成器函数，调用该函数会返回一个生成器对象
生成器函数是生成器工厂

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
        for word in self.words:  # 迭代self.words
            yield word  # 产出当前的word
        return

