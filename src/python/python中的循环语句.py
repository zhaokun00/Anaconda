
number = 10

count = 0

# 第一种方式的循环语句
"""
while(count < number):
    print("count = ",count)
    count = count + 1
"""

# while后面加else语句
# while(count < number):
#     print("count = ",count)
#     count = count + 1
# else:
#     print("已经大于等于10了")

"""
python中的for循环可以遍历任何序列中的项目,如一个列表或者一个字符串

for <variable> in <sequence>:
    <statements>
else:
    <statements>
"""

# 第二种循环语句

sites = ["Baidu", "Google","Runoob","Taobao"]

for sit in sites:
    print(sit)

# 如果需要遍历数字序列,可以使用内置range()函数,它会生成数列
for n in range(10):
    print(n)