"""
函数声明中的各个参数可以在:之后增加注解表达式。
如果参数有默认值，注解放在参数名和=之间
想注解返回值，在函数声明末尾的:之间添加一个->和表达式
注解最常用的类型是类和字符串

注解不会做任何处理，只是储存在函数的__annotations__属性（字典）中。return键保存的是返回值的注解
注解对Python解释器没有任何意义
"""


# 有注解的clip函数
def clip(text, *v, max_len: 'int >0' = 80, **d) -> str:
    """
    在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


print(clip.__annotations__)
