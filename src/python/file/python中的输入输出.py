
"""
python提供了input()内置函数从标准输入读入一行文本,默认的标准输入时键盘

input可以接收一个python表达式作为输入,并将运算结果返回
"""

# str = input("请输入:")
#
# print(str)

f = open("foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()




