"""
用于过滤的生成器函数：从输入的可迭代对象中产出元素的子集，不修改元素本身
    filter(predicate,it)  把it各值传给predicate，如果predicate(it)返回真值，则产出对应元素
    itertools.filterfalse(predicate,it)  与filter逻辑相反
    itertools.dropwhile(predicate,it) 跳过predicate(it)的计算结果为真的元素，然后产出剩下元素（不再做进一步检查）
    itertools.takewhile(predicate,it) 产出predicate(it)的计算结果为真的元素，然后立即停止（不再做进一步检查）
    itertools.compress(it,selector_it) 并行处理两个可迭代元素，如果selector_it中的元素为真，产出it对应的元素
    itertools.islice(it,stop) itertools.islice(it,start,stop,step=1) 产出it切片，惰性操作

用于映射的生成器函数：在输入的可迭代对象中的各个元素上做计算，返回结果
    itertools.accumulate(it,[func]) 产出积累的总和，如果提供了func，把前两个元素传给func，然后把计算结果和下一个元素传给func，最后产出结果
    enumerate(iterable,start=0) 产出由两个元素组成的元组，(index,item)，index从start开始计数，item从iterable获取
    map(func,it1,[it2...itN]) 把it的各元素传给func产出结果，或产出func(it1[n],it2[n])
    itertools.starmap(func,it) 把it中的各个元素传给func产出结果

用于合并的生成器函数:从输入的多个可迭代对象中产出元素
    itertools.chain(it1,...,itn) 先产出it1中所有元素，以此类推，无缝连接在一起。如果只传入一个可迭代对象，chain没什么作用
    itertools.chain.from_iterable(it) 产出it生成的各个可迭代对象元素，一个接一个无缝连接在一起。it应产出可迭代对象
    zip(it1,...,itn) 并行从输入的各个可迭代对象获取元素，产生由n个元素组成的元组，只要有一个可迭代对象到头了就默默停止
    itertools.zip_longest(it1,...,itn,fillvaule=None)  并行从输入的各个可迭代对象获取元素，产生由n个元素组成的元组,等到最长的可迭代对象到头后才停止，空缺由fillvaule填充
    itertools.product(it1,...,itn,repeat=1) 惰性计算笛卡儿积，从输入的各个可迭代对象获取元素，合并成由n个元素组成的元组，repeat指明重复处理多少次输入的可迭代对象

从一个元素产出多个值，扩展输入的可迭代对象
    itertools.count(start=0,step=1) 从start开始不断产生数字，步幅step
    itertools.repeat(item,[times])
    ...

产出输入可迭代对象的全部元素，以某种方式重新排列
    itertools.groupby(it,key=None) 产出由两个元素组成的元组，(key,group)，key是分组标准，group是生成器，用于产出分组里的元素
    itertools.reversed(seq) 倒序产生seq中的元素，seq必须是序列或实现了__reversed__特殊方法的对象
    itertools.tee(it,n=2) 产出一个由n个生成器组成的元组，每个生成器用于单独产出输入的可迭代对象中的元素
"""


# 用于过滤的生成器函数：从输入的可迭代对象中产出元素的子集，不修改元素本身
def vowel(c):
    return c.lower() in 'aeiou'


print(list(filter(vowel, 'Aardvark')))
import itertools

print(list(itertools.filterfalse(vowel, 'Aardvark')))
print(list(itertools.dropwhile(vowel, 'Aardvark')))
print(list(itertools.takewhile(vowel, 'Aardvark')))
print(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))))
print(list(itertools.islice('Aardvark', 4)))
print(list(itertools.islice('Aardvark', 4, 7)))

# 用于映射的生成器函数：在输入的可迭代对象中的各个元素上做计算，返回结果
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.accumulate(sample)))
print(list(itertools.accumulate(sample, min)))
print(list(itertools.accumulate(sample, max)))
import operator

print(list(itertools.accumulate(sample, operator.mul)))
print(list(itertools.accumulate(range(1, 11), operator.mul)))  # 计算各个数的阶乘
print(list(enumerate('albatroz', 1)))  # 从1开始为单词中字母编号
print(list(map(operator.mul, range(11), range(11))))  # 计数各整数的平方
print(list(map(operator.mul, range(11), [2, 4, 8])))  # 计数两个可迭代对象对应位置上两个元素的积，元素最少的可迭代对象到头后就停止
print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8])))  # 作用等同于zip
print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))  # 从1开始根据字母所在位置，把字母重复相应次数

# 用于合并的生成器函数:从输入的多个可迭代对象中产出元素
print(list(itertools.chain('ABC', range(2))))
print(list(itertools.chain(enumerate('ABC'))))  # 只传入一个可迭代对象，chain没什么作用
print(list(itertools.chain.from_iterable(enumerate('ABC'))))
print(list(zip('ABC', range(5), range(5, 8))))
print(list(itertools.zip_longest('ABC', range(5))))
print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))
print(list(itertools.product('ABC', range(2))))


# 产出输入可迭代对象的全部元素，以某种方式重新排列
print(list(itertools.groupby('LLLLAAAGG')))
for char,group in itertools.groupby('LLLLAAAGG'):
    print(char,'->',list(group))

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear','bat', 'dolphin', 'shark', 'lion']
for length,group in itertools.groupby(animals,len):
    print(length,'->',list(group))

print(list(itertools.tee('ABC')))
g1,g2 = itertools.tee('ABC')
print(list(zip(*itertools.tee('abc'))))