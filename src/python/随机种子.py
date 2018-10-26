import random

# 随机产生一个1-100之间的数值,每次运行时产生的随机数不相同
print(random.randint(1,100))

print("#################################")

# seed()方法改变随机数生成器的种子,可以在调用此函数
random.seed(111)
# 由于前面使用了seed函数,每次运行时产生的随机数是相同的
print(random.randint(1,100))