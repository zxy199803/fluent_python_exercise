"""
Python自带超过100种编解码器，用于文本和字节转换
"""
for codec in ['latin_1','utf_8','utf_16']:
    print(codec,'EL'.encode(codec),sep='\t')