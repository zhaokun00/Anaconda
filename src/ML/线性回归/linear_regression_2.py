import matplotlib.pyplot as plt
import numpy as np

__author__ = 'yasaka'

"""
# 计算某一列的数据的和
sum = np.random.rand(2,2)
print(sum)
# print(np.sum(sum[:,0]))
# 计算矩阵中所有的数据的和
# print(np.sum(sum))
"""

# 自己编写梯度下降法
X = 2 * np.random.rand(100, 1)
bias = np.random.randn(100, 1)

Y = 4 + 3 * X + bias

X_b = np.c_[np.ones((100, 1)), X]

# 定义学习率
learn_rate = 0.1
# 定义迭代次数
iterator = 1000
# 数据条数
total = 100

# 随机产生theta值,为2行1列的数据
theta = np.random.randn(2,1)

for it in range(iterator):
    # 更新theta值,该公式参考梯度下降的公式,公式会涉及到所有的样本数据
    gradient = 1 / total * X_b.T.dot(X_b.dot(theta)-Y)
    col = X_b.dot(theta) - Y
    # 计算所有行,第0列的值,可以看到总的误差值逐渐减小
    print(np.sum(col[:,0]))
    theta = theta - learn_rate * gradient

print(theta)

# 创建测试数据,创建了2条测试数据
X_test = np.array([[0], [2]])

X_test_b = np.c_[(np.ones((2, 1))), X_test]

# 由于创建了2条测试数据,因此预测值为2个值
y_predict = X_test_b.dot(theta)

print(y_predict)

plt.plot(X_test, y_predict, 'r-')
plt.plot(X, Y, 'b.')

plt.axis([0, 2, 0, 15])
plt.show()