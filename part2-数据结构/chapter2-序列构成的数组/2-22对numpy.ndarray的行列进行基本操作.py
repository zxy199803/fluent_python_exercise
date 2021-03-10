"""
NumPy 实现了多维同质数组和矩阵，这些数据结构不但能处理数字，还能存放自定义记录，可对元素进行高效操作

"""
import numpy

a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3, 4
print(a)
print(a[2])  # 从0开始
print(a[2][1])
print(a[2,1])
print(a[:,1])
print(a.transpose())