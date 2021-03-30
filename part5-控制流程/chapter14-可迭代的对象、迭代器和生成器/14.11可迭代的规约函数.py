"""
接受一个可迭代对象，返回单个结果
    all(it) it中所有元素为真值时返回True,all([])返回True
    any(it) it中有一个元素为真值时返回True,all([])返回False
    max(it,[key=],[default]) 返回it中的最大元素，key排序函数，可迭代对象为空返回default
    min(it,[key=],[default]) 返回it中的最小元素，key排序函数，可迭代对象为空返回default
    functools.reduce(fun,it,[initial])
    sum(it,start=0)
"""