"""
python看到的是不同的码位序列
unicodedata.normallize()
NFC 使用最少的码位构成等价字符串（w3c推荐形式）
NFKC 和 NFKD 用于搜索和索引，不要用于长期储存，两种转换导致数据损失 （用户搜索'1 ⁄ 2 inch'时，还能找到包含'½ inch' 的文档，）

保存文本前最好使用normallize('NFC',user_text)清洗字符串

大小写折叠：把所有文本变成小写
    s.lower()
    s.casefold()

去掉变音符号

"""
s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(s1 == s2)

from unicodedata import normalize, name

print(len(s1), len(s2))
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(normalize('NFC', s1) == normalize('NFC', s2))

ohm = '\u2126'
print(name(ohm))
ohm_c = normalize('NFC', ohm)  # 电阻单位欧姆被规范成希腊字母大写的欧米茄，比较时不相等
print(name(ohm_c))
print(ohm == ohm_c)
