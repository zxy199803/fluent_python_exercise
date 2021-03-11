"""
映射类型，如dict,collections.defaultdict,collections.OrderedDict

d.keys() 获取所有键
d.update(m,[**kargs]) m：映射或键值对迭代器，用来更新d里对应的条目 **kargs不确定数量的函数参数，相当于可容纳多个键值对的字典
update方法首先检查m是否有Keys方法，如果有update函数将其当作映射对象处理，否则把m当作包含键值对元素的迭代器。因此既可以用一个映射对象新建一个映射对象，还可以用可迭代对象来初始化一个映射对象

处理找不到的键
    d.setdefault(k,[default]) 若字典d里有键k，返回k所对应的值；若无,让d[k]=default,返回default
    可节省键查询次数
    my_dict.setdefault(key,[]).append(new_value)效果与下写法相同
    需进行2至3次键查询
    if key not in my_dict:
        my_dict[key]=[]
    my_dict[key].append(new_value)

d.get(k,[default]) 字典d里有键k，返回k所对应的值；若无,返回default或None
"""

import sys
import re

# 统计单词出现的行列
WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
for word in sorted(index, key=str.upper()):
    print(word, index[word])
# 减少查询的写法
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word,[]).append(location)


for word in sorted(index, key=str.upper()):
    print(word, index[word])