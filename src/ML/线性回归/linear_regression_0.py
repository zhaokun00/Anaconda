import numpy as np
import matplotlib.pyplot as plt

# https://blog.csdn.net/u010758410/article/details/71799142
# https://blog.csdn.net/yj1556492839/article/details/79031693
# https://blog.csdn.net/lanchunhui/article/details/51004387
# https://www.cnblogs.com/zhizhan/p/5615947.html
__author__ = 'yasaka'

# 这里相当于是随机X维度X1，rand是随机均匀分布
X = 2 * np.random.rand(100, 1)
#
# print("x的取值")
print(X)
#
# print("y的取值")
# 人为的设置真实的Y一列，np.random.randn(100, 1)是设置error，randn是标准正太分布
# y = 4 + 3 * X + np.random.randn(100, 1)

# print(y)
# 整合X0和X1
# X_b = np.c_[np.ones((100, 1)), X]
# print(X_b)

# 常规等式求解theta
# theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
# print(theta_best)

# 创建测试集里面的X1
# X_new = np.array([[0], [2]])
# X_new_b = np.c_[(np.ones((2, 1))), X_new]
# print(X_new_b)
# y_predict = X_new_b.dot(theta_best)
# print(y_predict)
#
# plt.plot(X_new, y_predict, 'r-')
# plt.plot(X, y, 'b.')
# plt.axis([0, 2, 0, 15])
# plt.show()

X_new = np.array([[0], [2]])

print(X_new)