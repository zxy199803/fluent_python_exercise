"""
标准库中的一些函数能接受字符串或字节序列作为参数

正则表达式
    使用字节序列构建，\d \w 只能匹配ASCII字符
    字符串模式，\d \w 能匹配ASCII之外的Unicode数字和字母
os函数


"""
import re

# 字节序列类型
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')
# 字符串类型
re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
text_str = "Ramanujan saw \u0be7\u0bed\u0be8\u0bef as 1729 = 1³ + 12³ = 9³ + 10³."
text_bytes = text_str.encode('utf_8')
print('Text', repr(text_str), sep='\n')
print('Numbers')
print(' str  :', re_numbers_str.findall(text_str))  # 字符串模式能匹配泰米尔数字
print(' bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
print(' str: ', re_words_str.findall(text_str))  # 字符串模式能匹配字母、上标、泰米尔数字和ASCII 数字
print(' bytes:', re_words_bytes.findall(text_bytes))
