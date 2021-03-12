"""
Python3的str对象获取的元素的Unicode字符
字符的标识(码位)，Unicode标准中以4-6个十六进制数字加前缀U+，如A的码位U+0041
具体的字符表述取决于编码（把码位转成字节序列的算法），如A编码成单字节\x41
字节序列转成码位：解码
"""
s = 'café'  # 有4个Unicode字符
print(len(s))
b=s.encode('utf8')  # 使用utf-8把str对象编码成bytes对象
print(b,len(b))
print(b.decode('utf8'))
