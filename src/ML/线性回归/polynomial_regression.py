import numpy as np
import matplotlib.pyplot as plt

# 导入多项式回归包
from sklearn.preprocessing import PolynomialFeatures
# 导入随机梯度下降包
from sklearn.linear_model import SGDRegressor

from sklearn.linear_model import LinearRegression

X = 200 * np.random.rand(500, 1)

bias = np.random.randn(500, 1)

# 构造数据
Y = 50 * X ** 2 + 3 * X + 4 + bias

plt.plot(X,Y,'r*')

# 创建一个多项式实例
# degree:多项式的阶数,即特征值的幂
# interaction_only:如果为True,会产生相互影响的特征集
# include_bias:是否包含偏差列
'''
对于只有一个特征,2阶
x x*x

如果对于有2个特征,2阶,将来构造的数据为
a,b,a *a,a *b ,b *b
'''
# 定义阶数和画线的颜色
# degree = {1:"g-",2:"r+",3:"y*"}

degree = {10:"y*"}

for index in degree:
    # 该处把截距去掉,原因在于在线性回归中有截距
    model = PolynomialFeatures(degree=index,include_bias=False)

    # 数据变换,输入的是一列数据,将来会产生2列数据
    X_T = model.fit_transform(X)

    # print(X)
    print(X_T)

    # 创建线性回归的实例,并默认有截距
    linear = LinearRegression(fit_intercept=True)

    # 传入的是有2个特征的数据
    linear.fit(X_T,Y)

    # 打印截距
    print(linear.intercept_)
    # 打印特征值的系数
    print(linear.coef_)

    # 预测
    y_predict = linear.predict(X_T)

    # print(X_T)
    # print(X_T[:, 0])

    # 绘制X与Y之间的关系
    plt.plot(X_T[:, 0], y_predict, degree[index])

plt.show()


