"""
散列表是稀疏数组，散列表的单元叫做表元(bucket)
在dict散列表中，每个键值对占用一个表元，每个表元两部分，一个是对键的引用，一个是对值的引用
所有表元大小一致，可以通过偏移量读取某个表元。Python设法保证约1/3的表元是空的，快到阈值时原有散列表会复制到一个更大空间
把一个对象放入散列表，首先用hash()计算这个元素键的散列值

1.散列值和相等性
内置hash()方法可用于所有内置类型对象，自定义对象调用hash()是运行自定义的__hash__
两对象比较时候相等，则其散列值必须相等。CPython中如果一个整型对象能存进一个机器字中，其散列值是它本身
越是相似但不相等的对象，其散列值的差别越大

2.散列表算法

"""