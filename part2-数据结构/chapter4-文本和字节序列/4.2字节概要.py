"""
Python内置两种基本二进制序列类型
不可变bytes类型
可变bytearray类型

其各元素是介于0-255(含)之间的整数，二进制序列的切片始终是同一类型的二进制序列

可打印的ASCII范围内字节，显示ASCII字符
制表，换行，回车，\，显示转义序列
其他字节值使用十六进制转义序列（如é显示\xc3\xa9）

可以使用字符串方法处理二进制序列，如endswith,upper
fromhex方法，解析十六进制数字对，构建二进制序列

memoryview 类用于共享内存，访问其他二进制序列无需复制字节序列
"""
cafe = bytes('café', encoding='utf8')  # bytes对象可以从str对象使用给的的编码构建
print(cafe)
print(cafe[0])  # 各个元素是整数
print(cafe[:1])  # 即使只有一个字节的切片也是bytes对象

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

print(bytes.fromhex('31 4B CE A9'))

# 使用数组中的原始数据初始化bytes对象
import array
numbers = array.array('h',[-2,-1,0])  # h短整数(16位)
octets = bytes(numbers)
print(octets)