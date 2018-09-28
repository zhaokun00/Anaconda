import numpy as np
import matplotlib.pyplot as plt
# 从sklearn.linear_model导入LinearRegression(线性回归模型)
from sklearn.linear_model import LinearRegression
__author__ = 'yasaka'

# 利用sklearn中的线性回归模型,来进行线性回归
# 随机生成100X3的数据,即100个样本3个特征
X = 2 * np.random.rand(1000, 3)
#产生一个100个元素的数据
bias = np.random.randn(1000)

# print(X)
#
# print(bias)
# 获取第0列数据
# print(X[:,0])
# 获取第1列数据
# print(X[:,1])
# 获取第2列数据
# print(X[:,2])

# Y = 4 + 1 * X[:,0] + 2 * X[:,1] + 3 * X[:,2] + bias

Y = 4 + X[:,0] + 2 * X[:,1] + 3 * X[:,2] + bias

print(Y.shape)

# print("y的取值")
# print(Y)

# 创建一个线性回归模型
# 在使用sklearn中的线性回归模型时,不用再添加X0(截距),在模型中会自动添加
linearRegression = LinearRegression()

# fit函数用于训练,如果样本数据太少,或者训练次数太少,则模型将会不准确
linearRegression.fit(X,Y)

# 存放的是回归系数
print(linearRegression.coef_)
# 存放的是截距
print(linearRegression.intercept_)
# 创建测试集,创建了一个2行1列的数据
X_test = np.array([[0,1,2], [2,2,3]])

# predict函数用于预测
y_predict = linearRegression.predict(X_test)
print(y_predict)

# plt.plot(X_test, y_predict, 'r-')
# plt.plot(X, Y, 'b.')
#
# plt.axis([0, 2, 0, 15])
# plt.show()