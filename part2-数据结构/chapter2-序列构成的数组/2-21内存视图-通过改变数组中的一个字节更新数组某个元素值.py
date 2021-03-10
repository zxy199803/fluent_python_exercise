"""
memeryview 内置类，能让用户在不复制内容的情况下操作同一数组的不同切片
是泛化和去数学化的Numpy，在不需要复制内容的前提下在数据结构间共享内存
应用场景：处理大型数据集合

即可原地直接操作内存
"""
import array

numbers = array.array('h', [0, 1, 2, 3, 4])  # h短整型有符号整数, 每个数字占两位，00，10，20，30，40
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')  # B无符号字符,memoryview.cast 用不同的方式读写同一块内存数据，内容字节不会随意移动
print(memv_oct.tolist())
memv_oct[5] = 4  # 把占两个字节的整数高位字节改成4
print(numbers)
