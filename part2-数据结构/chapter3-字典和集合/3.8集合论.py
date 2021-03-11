"""
set
    可用于去重
    元素必须是可散列的
    set本身不可散列
    a|b 合集；a&b 交集；a-b 差集 利用运算符减少循环和逻辑操作,速度

fronzenset
    可散列，因此可创建包含不同frozenset的set
    无{1，2，3}这样的字面量句法，只能采取构造的办法：frozenset(range(10))
"""
l = ['spam', 'spam', 'eggs', 'spam']
print(set(l))

# 邮箱地址集合haystack,较小邮箱地址集合needles。求needles有多少出现在haystack里
haystack = set(['1@', '2@', '3@'])
needles = set(['1@'])
print(len(haystack & needles))

# 集合的字符串表示形式
s = {1}  # 速度比s=set([1])快
print(type(s))
s.pop()
print(s)
s1 = {}  # 不要用这种方式创建空集，这样创建的是空字典
print(type(s1))
s2 = set()
print(type(s2))

# 集合推导
from unicodedata import name  # 获取字符的名字

Latin = {name(chr(i), '') for i in range(32, 256) if 'SIGN' in name(chr(i), '')}  # 每个字符的Unicode 名字里都有“SIGN”这个单词
print(Latin)


# 集合操作
