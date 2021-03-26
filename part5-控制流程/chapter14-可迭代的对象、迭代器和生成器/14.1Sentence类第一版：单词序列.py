"""
reprlib.repr用于生成大型数据结构的简略字符串表示

序列可迭代的原因:iter函数
    解释器需要迭代对象x时，会自动调用iter(x)
    内置的iter函数作用
        1.检查对象是否实现了__iter__方法，如果实现了就调用它获取一个迭代器
        2.如果没有实现__iter__方法，但是实现了__getitem__方法，Python会创建一个迭代器，尝试按顺序获取元素
        3.如果尝试失败，抛出TypeError异常，通常提示“object is not iterable”
任何Python序列可迭代的原因是实现了__getitem__方法。标准序列都实现了__iter__方法，我们也应该这么做

检查对象x能否迭代，最准确的方法是调用iter(x)函数，如果不可迭代再处理TypeError异常
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # 返回一个字符串列表，里面的元素是正则表达式的全部非重叠匹配

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence('the time has come')
print(s)
for word in s:  # Sentence可迭代
    print(word)

print(list(s))  # 因为可迭代，Sentence对象可以用于构建列表和其他可迭代类型

# 这版Sentence类也是序列，可以按索引获取单词
print(s[0])