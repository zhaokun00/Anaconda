import numpy as np
import matplotlib.pyplot as plt

# 导入岭回归包
from sklearn.linear_model import ElasticNet
# 导入随机梯度下降包
from sklearn.linear_model import SGDRegressor

X = 2 * np.random.rand(100, 1)

bias = np.random.randn(100, 1)

Y = 4 + 3 * X + bias

"""
# 示例1:第一种lasso回归的方式
# 创建一个岭回归的对象,alpha参数:L1正则项中的aplha,max_iter:最大迭代次数
ridge = ElasticNet(alpha=0.0001, l1_ratio=0.55,max_iter=10000)
# 训练数据
ridge.fit(X,Y)

# 打印截距
print(ridge.intercept_)
# 打印参数W
print(ridge.coef_)

X_test = np.array([[0], [2]])
# 预测数据
Y_test = ridge.predict(X_test)

plt.plot(X, Y, 'b.')
plt.plot(X_test, Y_test, 'r-')

plt.show()

"""

# 示例2:直接使用梯度下降法进行岭回归,penalty参数:使用的是哪种正则惩罚项,alpha:L1的alpha参数,n_iter:迭代次数
# 使用SGDRegressor可以替代Ridge Regtession、Lasso、Elastic Net三种回归方法

ridge = SGDRegressor(penalty="elasticnet", alpha=0.001,l1_ratio=0.15,n_iter=1000)
# 训练数据
ridge.fit(X,Y)

# 打印截距
print(ridge.intercept_)
# 打印参数W
print(ridge.coef_)

X_test = np.array([[0], [2]])
# 预测数据
Y_test = ridge.predict(X_test)

plt.plot(X, Y, 'b.')
plt.plot(X_test, Y_test, 'r-')

plt.show()
