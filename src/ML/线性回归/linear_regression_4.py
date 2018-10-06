import numpy as np
# 导入归一化包
from sklearn.preprocessing import MinMaxScaler
# 导入标准化包
from sklearn.preprocessing import StandardScaler

from numpy import float64
__author__ = 'yasaka'

"""
# 示例1:在python中的list类型中求解最小值和最大值
X = [100,2,3,4]
# print(X)

# min函数:计算列表中的最小值
# print(min(X))
# max函数:计算列表中的最大值
# print(max(X))
# index函数:计算元素的下标
# print(X.index(min(X)))

# 对于python中list类型不能直接进行运算操作
# print(X + 1)
# print(X > 30)

"""

"""
# 示例2:在numpy中计算最大值最小值
# 5行一列的数据
X = np.random.rand(5, 1)
# print(X)
# numpy中求解最小值,获取整个矩阵的最小值
# print(X.min())
# numpy中求解最大值,获取整个矩阵的最大值
# print(X.max())

# 5行2列的数据
XX = np.random.rand(5, 2)
# print(XX)
# numpy中求解最小值,获取整个矩阵的最小值
# print(XX.min())
# numpy中求解最大值,获取整个矩阵的最大值
# print(XX.max())

# 第0行、所有列数据
# print(XX[0,])
# 所有行、第0列数据
# print(XX[:,0])

# len函数:计算元素的个数,第0行数据有多少个
# print(len(XX[0,]))

# len函数:计算第0列数据元素的个数
# print(len(XX[:,0]))

Y = np.random.rand(5, 1)
# print(Y)
# 每个元素在原有的基础上+1
# print(Y + 1)

Y = np.random.rand(5, 2)
# print(Y)
# 每个元素在原有的基础上+1
# print(Y + 1)

Y = np.random.rand(5, 2)
# print(Y)
# 每个元素在原有的基础上*2
# print(Y * 2)

Y = np.random.rand(5, 2)
# print(Y)
# 比较矩阵中的每一个元素与0.5比较
index = Y < 0.5
# 返回的为矩阵的形式.返回的结果是True,False两种结果
# print(index)
# 打印返回结果为True的值
# print(Y[index])

"""


# 示例3:归一化操作,在一列数据上进行归一化操作

X = [1.,2.,3.]

# Y = np.array([
#               [1., 1., 2.],
#               [0., 0., 4.],
#               [2., 0.5, 4.],
#               ])

Y = np.array(X).reshape(3,1)
# print(Y.shape)
# print(Y)

# feature_range设置最大最小值,默认为(0,1)
scaler = MinMaxScaler(feature_range=(1,2))

Z = scaler.fit_transform(Y)

print(Z)


"""
# 标准化
X = np.array([1.,2.,3.]).reshape(3,1)

# print("数据:",X)
# print("均值:",np.mean(X))
# print("标准差:",np.std(X))

# 手动计算标准化
# print((X-np.mean(X)) / np.std(X))
scaler = StandardScaler()

# API计算标准化
Z = scaler.fit_transform(X)
# print(Z)

# 计算二维数组
Y = np.array([
              [1., 1., 2.],
              [0., 3., 4.],
              [2., 0.5, 4.]
              ])

Z = scaler.fit_transform(Y)
print(Z)

Z = scaler.fit_transform(Y[:,0])
print(Z)

Z = scaler.fit_transform(Y[:,1])
print(Z)

Z = scaler.fit_transform(Y[:,2])
print(Z)

"""

# 示例4:numpy中进行计算平均值
"""
Y = np.array([1,2,3])
# 计算一维数组的平均值
print(np.mean(Y))

Y = np.array([
              [1,2,3],
              [4,5,6]
            ])

# 计算元素的个数
print("size:",Y.size)
# 计算元素的求和
print("sum:",Y.sum())
# 计算元素的平均值
print("mean:",Y.sum()/Y.size)
# 使用API函数计算平均值
print(np.mean(Y))

# axis=0时计算每列数据的平均值
print(np.mean(Y,axis=0))
# axis=1时计算每行数据的平均值
print(np.mean(Y,axis=1))
"""

# 示例5:计算方差与标准差
"""
# 计算一维数组
X = np.array([1,2,3])
print("X:",X)
Y = np.mean(X)
print("mean:",Y)

# 方差函数var()相当于函数mean(abs(x - x.mean())**2),其中x为矩阵。
print("计算方差:",np.mean(np.square(X-Y)))
print("API方差:",np.var(X))

# std()相当于sqrt(mean(abs(x - x.mean())**2))，或相当于sqrt(x.var())。
print("计算标准差:",np.sqrt(np.mean(np.square(X-Y))))
print("API标准差:",np.std(X))
"""

# 计算二维数组
"""
X = np.array([
              [1,2,3],
              [4,8,5]
            ])


Y = np.mean(X,axis=0)
print("mean:",Y)

print("API方差:",np.var(X,axis=0))
print("API标准差:",np.std(X,axis=0))

"""

# 示例6:计算中值
# 中值指的是将序列按大小顺序排列后,排在中间的那个值,如果有偶数个数,则是排在中间两个数的平均值

# 计算一维数组的中值
"""
X = np.array([
              [8,2,3]
            ])

print(np.median(X))

# 计算二维数组的中值
X = np.array([
              [1,2,3],
              [4,5,6]
            ])

print(np.median(X,axis=0))
"""



