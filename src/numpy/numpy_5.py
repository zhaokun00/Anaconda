import numpy as np
import  pandas as pd
from pandas import  Series,DataFrame

# 示例1:linspace函数,在指定的间隔内返回均匀间隔的数字
# start:序列的开始点
# stop:序列的结束点
# num:生成的样本数,默认是50
# endpoint:如果为真,则一定包括stop,如果为False,一定不会有stop

"""
data = np.linspace(1,100,num = 100)
print(data)
"""

# 示例2: ndarray与list相互转换

"""
list = [1,2,3]

# 类型是一个列表
print(list)

array = np.array(list)

# 类型是ndarray类型,相当于矩阵形式
print(np.array(array))

# 将ndarray类型转换为list类型
list1 = array.tolist()

print(list1)
"""

# 示例3:ndarray与Series,DataFrame相互转换

# 定义一个列表,这种形式相当于列表嵌套列表的形式
data = [
       [1,'zhaokun'],
       [2,'ycl'],
       [3,'aimi']
]

#相当于数据库中的一条一条数据
# 将列表形式转换为Series类型
ser = Series(data,index=['A','B','C'])

print(ser)
print(type(ser))

# DataFrame类型相当于数据库中的表
# index:定义行标号,columns:定义列标号
df = DataFrame(data,index=['A','B','C'],columns=['id','name'])

print(df)

# 将Series类型转换为list类型
n = ser.as_matrix()
print("n's type = ",type(n))
print(n)
print(n[0])

# 将DataFrame类型转换为ndarray类型,
n = df.as_matrix()
# 可以指定列名称
# n = df.as_matrix(columns = ['id','name'])
print(n)

# 将DataFrame类型转换为ndarray类型
n = df.values
print(n)