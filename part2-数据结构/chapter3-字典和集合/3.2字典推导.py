"""
字典推导(dictcomp)从任何以键值对作为元素的可迭代对象中构建出字典
"""
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'US'),
]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
print({code: country.upper() for country, code in country_code.items() if code < 87})
