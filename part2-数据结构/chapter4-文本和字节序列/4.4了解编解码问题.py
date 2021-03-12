"""
编解码器的错误处理方式可扩展，

UnicodeEncodeError
    若目标编码中没有定义某个字符

UnicodeDecodeError
    遇到无法转换的字符序列

SyntaxError
    Python3默认使用UTF-8编码源码，加载的.py模块包含UTF-8外的数据且没有声明编码

Chardet包可以分析使用了哪种编码

BOM(字节序标记)，指明是否是小字字节。字节序只对一个字占多个字节的编码有影响
"""
city = 'São Paulo'
print(city.encode('cp437',errors='ignore'))  # 跳过无法编码的字符
print(city.encode('cp437',errors='replace'))  # 用?替代无法编码的字符
print(city.encode('cp437',errors='xmlcharrefreplace'))  # 把无法编码的字符替换成XML实体

# UnicodeDecodeError
octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('utf8'))