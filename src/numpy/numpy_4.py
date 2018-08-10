import numpy as np

# 示例1:计算指数与开方运算

"""
array1 = np.arange(5)

print(array1)

# 以e为底,array1为幂
print(np.exp(array1))

# 开平方
print(np.sqrt(array1))
"""

# 示例2: numpy中的floor函数
"""
array1 = 10 * np.random.random((3,4))

print(array1)

# 取整操作
a = np.floor(array1)

print(a)
"""

# 示例3：numpy中的hstack函数,按照行进行矩阵的组合,vstack按照列进行组合

"""
a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((2,2)))

print(type(a))

print(a)
print(b)

c = np.hstack((a,b))
print(c)

d = np.vstack((a,b))

print(d)
"""

# 示例4:numpy中的ravel函数与resize函数

"""
a = np.floor(10*np.random.random((2,3)))

print(a)
print(np.shape(a))

# 恢复成1维矩阵
vector1 = np.ravel(a);
print(vector1)

# 重新定义矩阵的行与列
print(np.resize(vector1,(3,2)))
"""

# 示例5:矩阵的拷贝
# a,b为同一个对象
a = np.floor(10*np.random.random((2,3)))
b = a
print(id(a))
print(id(b))

# 矩阵的拷贝,a、c为2个对象
c = np.copy(a)

print(id(c))