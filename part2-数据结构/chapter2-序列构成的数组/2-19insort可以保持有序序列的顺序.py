"""
排序很耗时，得到有序序列后最好保持其有序
insort(seq,item) 将item插入seq，并保持seq升序
"""
import bisect
import random

SIZE = 7
random.seed(1729)  # seed()指定随机数生成时所用算法开始的值，相同的seed每次生成的随机数都相同，否则因时间差异而不同

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)  # 该方法从给定范围返回一个随机项
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
