"""
队列(queue)，只允许在表的前端删除，在后端(rear)插入
双向队列，允许两头进出
删除列表第一个元素之类的操作很耗时，牵扯到移动所有元素
collections.deque类（双向队列）是一个线程安全，可快速从两端增删元素的数据类型
可用来存放最近用到的几个元素，因可指定队列大小，满员后可从反向端删除过期元素
实现了大部分列表所拥有的方法，从中间删除和操作元素会慢,只对头尾操作做了优化
deque可在多线程程序安全的当作先进先出队列使用，不需担心资源锁
"""
from collections import deque
dq=deque(range(10),maxlen=10)
print(dq)
dq.rotate(3)  # 旋转操作，rotate(n),n>0最右边的的n个元素移动到队列左边
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)  # 对以满队列头部添加元素，尾部元素会删除
print(dq)
dq.extend([11,22,33])  # 挤掉了头部三个元素
print(dq)
dq.extendleft([10,20,30,40])  # 把迭代器里的元素逐个添加到左侧，因此在队列中逆序出现
print(dq)
print(dq[5])