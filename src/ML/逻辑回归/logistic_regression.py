import numpy as np
from sklearn import datasets
from sklearn.linear_model import  LogisticRegression
import  matplotlib.pyplot as plt
from time import time

iris = datasets.load_iris()

print("type:",type(iris))

# print(iris)
# print("keys:")
# print(list(iris.keys()))
# print("desc:")
# print(iris['DESCR'])
# print("feature:")
# print(iris['feature_names'])
#
# print(iris)

# 获取第3列特征数据
X = iris['data'][:,3:]
# print(X)

# 获取标签数据,分类的列别
Y = iris['target']
# print(Y)

# 创建逻辑回归的实例,该实例不仅仅能进行二分类的问题,还能进行多分类的问题
# max_iter: 最大迭代次数，这个是硬限制，它的优先级要高于tol参数，不论训练的标准和精度达到要求没有，都要停止训练。默认值是-1，指没有最大次数限制
# 具体其他参数可以查看sklearn官方文档的API
log_reg = LogisticRegression(multi_class='ovr',solver='sag')

log_reg.fit(X,Y)

X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
print(X_new)

# predict_proba返回的是一个n行k列的数值,第i行第j列上的数值是模型预测第i个预测样本为某个标签的概率并且每一行的概率和为1
# 比较的概率当哪个概率最大将会取哪一个类别
y_proba = log_reg.predict_proba(X_new)
print(y_proba)

# 预测新数据的列别
y_hat = log_reg.predict(X_new)
print(y_hat)

plt.plot(X_new, y_proba[:, 2], 'g-', label='Iris-Virginica')
plt.plot(X_new, y_proba[:, 1], 'r-', label='Iris-Versicolour')
plt.plot(X_new, y_proba[:, 0], 'b--', label='Iris-Setosa')

plt.show()




