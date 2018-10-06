"""
python中的字符串用单引号'或双引号"括起来,同时使用反斜杠\转义特殊字符

字符串的截取的语法格式如下:
变量[头下标:尾下标]
备注:下标是从0开始的,不包括尾下标的字符
"""

# 示例1
str = "zhaokun"

# 打印整个字符串
print("str = ",str)
# 打印从下标0到下标2的字符,不包括下标2的字符
print("str[0:2]",str[0:2])
# 打印从下标1到最后的字符
print("str[1:]",str[1:])


# 示例2

"""
加号+是字符串的连接符
"""
name = "zhaokun"
print(name + "is male")

# 示例3

"""
python使用反斜杠转义特殊字符,如果不想让反斜杠发生转义,可以在字符串前面添加一个r,表示原始字符串
"""

print("zhaokun\nycl")
print(r"zhaokun\nycl")

"""
python字符串格式化
python支持格式化字符串输出,尽管这样可能会用到非常复杂的表达式,但最基本的用法是将一个值插入到一个有
字符串格式符中
"""
print("name = %s,age = %d"%("赵坤",30))

# 示例4 字符串的join函数:用于将指定字符连接序列中元素后生成的新字符串

str = "-"
sque = ("a","b","c")

result = str.join(sque)
print(result)


