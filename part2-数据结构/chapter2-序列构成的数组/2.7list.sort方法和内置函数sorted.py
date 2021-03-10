"""
list.sort 就地排序列表，不会把原列表复制一份，因此返回None
若对对象进行就地改动，应返回None。弊端是无法将其串联起来调用
sorted，创建一个新列表作为返回值，不管sorted接受怎样的参数，最后都返回一个列表

可选关键字参数
reverse True 降序输出，默认False
Key 如key=str.lower实现忽略大小写排序,key=len基于字符串长度排序
"""
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)
print(sorted(fruits,key=len))
print(sorted(fruits,key=len,reverse=True))  # 不是sorted(fruits,key=len)的完全反转，在长度一样时，grape和apple相对位置不变
fruits.sort()
print(fruits)