"""
slice.indices方法开放了内置序列实现的棘手逻辑，用于处理缺失索引，负数索引，长度超过目标序列的切片
"""

class MySeq:
    def __getitem__(self, index):
        return index


s = MySeq()
print(s[1])
print(s[1:4])
print(s[1:4:2])  # 步幅为2
print(s[1:4:2, 9])  # []中有逗号，__getitem__收到的是元组
print(s[1:4:2, 7:9])  # 元组中有多个切片对象

print(slice)  # slice是内置类型
print(dir(slice))
help(slice.indices)  # 给定长度为len的slice，计算slice的起始和结尾索引、步幅。超出边界的索引会被裁掉

print(slice(None,10,2).indices(5))  # 'ABCDE'[:10:2]等同于'ABCDE'[:5:2]
print(slice(-3,None,None).indices(5))  # 'ABCDE'[-3:]等同于'ABCDE'[2:5:1]
