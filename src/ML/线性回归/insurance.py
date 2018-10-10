import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from pandas import DataFrame
# 示例:保险案例,利用多项式回归和线性回归,预测保险
# 读取数据
data = pd.read_csv("./insurance.csv")

# 打印数据类型,DataFrame类型相当于一个表格
# print("type:",type(data))
# 打印数据描述
# print("des:",data.describe())

# 打印年龄相同的个数
data_count = data["age"].value_counts()
# print(data_count)
# 打印前10行数据
# print(data["age"].head(10))

# 打印后10行数据
# print(data["age"].tail(10))

# 画直方图
# 画直方图的目的:因为年龄该特征值与标签之间相关性很大,因此可以通过画直方图的形式,看样本数据中各个年龄段的样本都为多少
# 在训练模型时候,读取数据集时要包含各个年龄段的数据并且各个年龄段的数据要均匀以防止过拟合
# data_count[:10].plot(kind='bar')
# 保存图片在显示图片之前,如果在显示后面则保存图片为空白图片
# plt.savefig('./temp')
# plt.show()

# 列和列之间的相关性
print(data.corr())

x = data[['age', 'bmi', 'children']]
y = data['charges']

# print(x)
# print(type(x))

# 生成多项式实例
poly_features = PolynomialFeatures(degree=3, include_bias=False)
# 进行数据转换
X_poly = poly_features.fit_transform(x)

reg = LinearRegression()
# 训练数据
reg.fit(X_poly, y)
print(reg.coef_)
print(reg.intercept_)

y_predict = reg.predict(X_poly)

# 画age与真实值y之间的关系
plt.plot(x['age'], y, 'b.')
# 画age与预测值y之间的关系
plt.plot(X_poly[:, 0], y_predict, 'r.')

plt.show()

# 示例:将DataFrame结构类型转换为ndrray类型
x1 = [[1,10],[2,15],[3,17]]
x1 =np.array(x1)
# 将DataFrame转换为ndarray结构
df = DataFrame(x1,index=['1','2','3'],columns=['A','B'])
print(df)
print(df.corr())

