import numpy as np

# 示例1:测试numpy中的arange函数,产生一个一维数组,可以规定起始值,结束值,步长,数据类型

"""
array1 = np.arange(15)

print(array1)

"""

# 示例2:测试numpy中的reshape函数,将某维的矩阵转换为某维的矩阵

"""
array1 = np.arange(15)

# 将其转换为3行5列的二维数组
array1 = array1.reshape(3,5)

print(array1.shape)

print(array1)

"""

# 示例3:计算矩阵的维度

"""
array1 = np.arange(15)

array1 = array1.reshape(3,5)

print(np.ndim(array1))
print(array1.ndim)
"""

# 示例4: 计算矩阵中数据的类型

"""
array1 = np.arange(15)

array1 = array1.reshape(3,5)

# 以下两种方式是相同的
print(array1.dtype)
print(array1.dtype.name)
print(array1.dtype == np.int32)
"""

# 示例5：计算矩阵中元素的个数

"""
array1 = np.arange(15)

array1 = array1.reshape(3,5)

print(np.size(array1))

# 计算一行有多少元素
print(np.size(array1,1))

# 计算以列有多少元素
print(np.size(array1,0))
"""

# 示例6：计算两个矩阵的形状是否相同
"""
array1 = np.arange(4)

array1 = array1.reshape(2,2)

shape1 = np.shape(array1)

print(array1)
print(shape1)

array2 = np.arange(4,8)

array2 = array2.reshape(2,2)

shape2 = np.shape(array2)

print(array2)
print(shape2)

# shape为tuple类型
print(type(shape1))

# 打印形状是相等的
print(shape1 == shape2)

"""

# 示例7:产生一个元素都为0的矩阵

"""
array1 = np.zeros((3,3),np.int32)
print(array1)
"""

# 示例8:产生一个元素都为1的矩阵

"""
array1 = np.ones((3,3),np.int32)
print(array1)
"""

# 示例9:随机产生一个元素在0-1之间的矩阵,函数random的用法

"""
array1 = np.random.random((3,3))
print(array1)
"""

# 示例9:产生一个一维矩阵,执行起始位置、结束位置、个数

"""
array1 = np.linspace(10,100,10)
print(array1)
"""

# 示例10:numpy中的sin函数

"""
from numpy import pi

array1 = np.linspace(0,2 * pi,100)

print(array1)

array1 = np.sin(array1)

print(array1)
"""

# 示例11:矩阵的运算

A = np.array( [[1,1],
               [0,1]] )
B = np.array( [[2,0],
               [3,4]] )

print(A)
print(B)

# 矩阵的直接相乘,对应的各个元素之间相乘
print(A * B)

# 矩阵的内积
print(np.dot(A,B))

# 矩阵的转置
print(A.T)
