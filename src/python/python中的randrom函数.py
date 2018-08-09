"""
random()方法返回随机生成的一个实数,它在[0,1)范围内

语法:
import random

random.random()

注意:random()是不能直接访问的,需要导入random模块,然后通过random静态对象调用该方法
"""

import random

# 产生一个0到1之间的随机浮点数
print("随机数:",random.random())

# 产生一个1到100的一个整数型随机数
print("随机数:",random.randint(1,100))

# 产生一个从100到200间隔为5的随机整数
print("随机数:",random.randrange(100,200,5))

# 随机从序列中选取一个元素
str = "12345"
print("随机数:",random.choice(str))
list = ("a","b","c")
print("随机数:",random.choice(list))

# 产生一个从2.0到3.0之间的随机浮点数,区间可以不是整数
print("随机数:",random.uniform(2.0,3.0))


