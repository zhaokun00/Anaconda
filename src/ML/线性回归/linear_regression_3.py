import numpy as np

__author__ = 'yasaka'

# 随机梯度下降法
X = 2 * np.random.rand(100, 3)
# bias = np.random.randn(100, 3)
# Y = 4 + 5 * X + bias

bias = np.random.randn(100)

Y = 4 + X[:,0] + X[:,1] + 3 * X[:,2] + bias

X_b = np.c_[np.ones((100, 1)), X]

# 获取X的第一行数据
# print(X_b[0:1])

# 定义学习率
learn_rate = 0.1
# 定义迭代次数
iterator = 1000
# 数据条数
total = 100

theta = np.random.randn(4,1)

t0=5
t1=50
# 定义学习率函数
def learning_schedule(t):
    return t0 / (t + t1)

# 第一层循环:迭代次数
for it in range(iterator):
    # 第二层循环:计算梯度值,循环次数可以
    for i in range(total):
        # 从样本数据中随机挑选一条数据,用于计算梯度,该层循环次数可以进行调整
        index = np.random.randint(total)
        # 从当中抽取一条样本数据
        xi = X_b[index:index+1]
        yi = Y[index:index+1]
        # 计算梯度值,得到的是一个矩阵,每一个theta值
        gradient = xi.T.dot(xi.dot(theta) - yi)
        print(gradient)
        # 学习率随着迭代次数的增多,逐渐减小
        learn_rate = learning_schedule(it*total + i)
        print("learn_rate=",learn_rate)
        theta = theta - learn_rate * gradient

print(theta)
# 创建测试数据,创建了2条测试数据
# X_test = np.array([[0], [2]])
#
# X_test_b = np.c_[(np.ones((2, 1))), X_test]
#
# # 由于创建了2条测试数据,因此预测值为2个值
# y_predict = X_test_b.dot(theta)
#
# print(y_predict)
#
# plt.plot(X_test, y_predict, 'r-')
# plt.plot(X, Y, 'b.')
#
# plt.axis([0, 2, 0, 15])
# plt.show()
