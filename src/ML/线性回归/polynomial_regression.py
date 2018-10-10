import numpy as np
import matplotlib.pyplot as plt

# 导入多项式回归包
from sklearn.preprocessing import PolynomialFeatures
# 导入随机梯度下降包
from sklearn.linear_model import SGDRegressor

from sklearn.linear_model import LinearRegression

X = 2 * np.random.rand(500, 1)

bias = np.random.randn(500, 1)

# 构造数据
Y = 50 * X ** 2 + 3 * X + 4 + bias

# plt.plot(X,Y,'b.')
# plt.show()

model = PolynomialFeatures(degree=2,include_bias=False)

X_T = model.fit_transform(X)

# print(X)
# print(X_T)

linear = LinearRegression()

linear.fit(X_T,Y)

print(linear.intercept_)
print(linear.coef_)

y_predict = linear.predict(X_T)

plt.plot(X_T, y_predict, 'b.')

plt.show()


