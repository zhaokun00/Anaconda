import numpy as np
import matplotlib.pyplot as plt

# https://blog.csdn.net/u010758410/article/details/71799142
# https://blog.csdn.net/yj1556492839/article/details/79031693
# https://blog.csdn.net/lanchunhui/article/details/51004387
# https://www.cnblogs.com/zhizhan/p/5615947.html
__author__ = 'yasaka'

##############################################################################
# 基础知识
"""
numpy中有一些常用的用来产生随机数的函数,randn()和rand()就属于其中
np.random.random(size)生成[0.1)之间的浮点数,size是浮点数的个数
np.random.rand(d0,d1,...,dn)的随机样本为[0,1)中,dn表示维度
np.random.randn(d0,d1,...,dn)是从标准正太分布中返回一个或多个样本值

"""
# 产生2个[0,1)之间的随机数
# x1 = np.random.random(2)
# ndarray数据结构就相当于矩阵的形式,有1维的矩阵、2维的矩阵...n维的矩阵
# print(x1,type(x1))

# 产生一个2X2的矩阵即2行2列,数值在[0,1)之间
# x1 = np.random.rand(2,2)
# print(x1,type(x1))

# 产生一个2X3的矩阵即2行3列,数值可正可负
# x1 = np.random.randn(2,3)
# print(x1,type(x1))

# randint(low, high=None, size=None, dtype='l')
# 返回随机整数，范围区间为[low,high），包含low，不包含high
# 参数：low为最小值，high为最大值，size为数组维度大小，dtype为数据类型，默认的数据类型是np.int
# high没有填写时，默认生成随机数的范围是[0，low)
# x1 = np.random.randint(1,100,10)
# print(x1)

# 产生一个100X1的矩阵即100行1列,数值在[0,1)之间
# X = 2 * np.random.rand(100, 1)

# print("X取值:")
# print(X)

# 随机生成的偏移量也是100X1的数据
# bias = np.random.randn(100, 1)
# print("bias取值:")
# print(bias)

# 创建一个数据全部是1的数组,数据类型是ndarray类型
# 创建一个100X1的二维数组,即100行1列
# print(np.ones((100, 1)))

'''
2,1,3
2:代表的是3维数组里面有2个二维数组
1:代表的是2维数组里面有1个一维数组
3:代表的是1维数组里面有3个特征值
[
[[1. 1. 1.]]

[[1. 1. 1.]]
]

2,2,3
[
[[1. 1. 1.]
 [1. 1. 1.]]

[[1. 1. 1.]
[1. 1. 1.]]
]
'''
# print(np.ones((2 ,1 ,3)))

# 创建一个数据全部是0的数组
# 创建的是元素个数是5的一维数组
# print(np.zeros(5))

#
# np.c_:是按行连接两个矩阵,就是把两矩阵左右相加,要求行数相等,类似于pandas中的merge,增加的列数
# np.r_:是按行连接两个矩阵,就是把两矩阵上下相加,要求列数相等,类似于pandas中的concat(),增加的行数

# x1 = np.array([1,2,3])
# x2 = np.array([4,5,6])
#
# print(np.r_[x1,x2])
# print(np.c_[x1,x2])

# x1 = np.array([[1,2,3],[4,5,6]]);
# print(x1)
# .T操作:矩阵的转置操作
# print(x1.T)

# x2 = np.array([1,2])
# dot矩阵的内积
# print(x2.dot(x2.T))

# 利用列向量与行向量产生一个nXn的矩阵
# x1 = np.arange(5)
# print(x1,len(x1))
#
# x2 = x1.reshape(1,len(x1))
# print(x2,x2.shape)
#
# x3 = x1.reshape(len(x1),1)
# print(x3,x3.shape)
# print(x3.dot(x2))

# 产生从0-10之间的数值
# x1 = np.arange(10)
# print(x1)
# 产生从10-20之间的数值
# x1 = np.arange(10,20)
# print(x1)
# 产生从10-20之间的数值,步长为2
# x1 = np.arange(10,20,2)
# print(x1)

# reshape:产生指定的矩阵,2行5列
# x1 = np.arange(10).reshape(2,5)
# print(x1)

# 计算矩阵的逆矩阵
# x1 = np.array([-2,1,4,-3]).reshape(2,2)
# print(np.linalg.inv(x1))

# 计算矩阵的行列式
# print(np.linalg.det(x1))

# 计算矩阵的范数
# x1 = np.array([1,2])
#
# print(np.linalg.norm(x1,ord=1))
# print(np.linalg.norm(x1,ord=2))
# print(np.linalg.norm(x1,ord=np.inf))

##############################################################################
# 利用解析解的方式进行线性回归
X = 2 * np.random.rand(100, 1)
print("X shape:",X.shape)
bias = np.random.randn(100, 1)
print("bias shape:",bias.shape)
# X与Y之间的真实关系,产生的Y是100X1的矩阵,即100行1列的数据,由于随机加上了偏移值,因此X与Y之间的关系并不是直线关系
# X与Y之间虽然不是线性关系,但是咱们要用线性的方式去拟合非线性的关系
# Y的形状为m行1列数据
Y = 4 + 3 * X + bias
print("Y shape:",Y.shape)
# print("y的取值")
# print(Y)

# 整合X0和X1,将其变成100行2列的数据,第一列数据是X0,相当于截距
X_b = np.c_[np.ones((100, 1)), X]
# print(X_b)

# 利用解析解的方式,计算theta值,里面包含所有的样本数据(特征值与标签值),计算公式可参考
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(Y)
# 计算出theta值后可以和实际公式中的参数进行比较
print(theta_best)


# 创建测试集,创建了一个2行1列的数据
X_test = np.array([[0], [2]])
# 数据进行拼接
X_test_b = np.c_[(np.ones((2, 1))), X_test]
# 根据上面计算的theta值和x值计算y值
y_predict = X_test_b.dot(theta_best)
# print(y_predict)
#
plt.plot(X_test, y_predict, 'r-')
plt.plot(X, Y, 'b.')
# 设置X与Y的取值范围
plt.axis([0, 2, 0, 15])
plt.show()