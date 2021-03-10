"""
存放大量浮点数时，数组(array)效率更高，其背后不是float对象，而是数字的机器翻译，即字节表述
需频繁对序列做先进先出操作，双端序列(deque)更快
包含操作(如检查某一元素是否出现在集合)，set对此做过优化更合适，但set是无序的

数组支持所有可变序列的操作，还提供读写的更快方法
创建数组需要类型码，python不允许存放指定类型外的数据
数组不支持list.sort()就地排序
"""

from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])
fp = open('floats.bin', 'wb')  # 写入二进制文件比以每行一个浮点数写入文本文件快7倍，且省空间
floats.tofile(fp)
fp.close()
floats2 = array('d')  # d说明类型
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 7)  # 从二进制文件读取比从文本文件快60倍，后者使用内置的float方法把每一行文字转换成浮点数
fp.close()
print(floats2[-1])
print(floats == floats2)
