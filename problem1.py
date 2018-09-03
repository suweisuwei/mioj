#coding:utf-8
# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    num = int(line)

    # 返回处理后的结果
    return get_count(num)

def get_count(num):
    if num == 1 :
        return 1
    elif num == 2 :
        return 2
    else :
        return get_count(num - 1) + get_count(num - 2)

result = solution(5)
print(result)

