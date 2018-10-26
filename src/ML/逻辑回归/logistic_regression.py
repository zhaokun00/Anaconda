import numpy as np
from sklearn import datasets
from sklearn.linear_model import  LogisticRegression
import  matplotlib.pyplot as plt
from time import time

'''
# 示例1: 逻辑回归,多分类,并有一个特征值
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
# tol:残差收敛条件，默认是0.0001，也就是只需要收敛的时候两步只差＜0.0001就停止，可以设置更大或更小。(逻辑回归模型的损失函数是残差平方和)
# C:正则化系数，正则化强度的导数，必须是一个正数，值越小，正则化强度越大，即防止过拟合的程度更大
# random_state:随机种子的设置，默认是None,如果设置了随机种子，那么每次使用的训练集和测试集都是一样的，这样不管你运行多少次，最后的准确率都是一样的；如果没有设置，那么每次都是不同的训练集和测试集，最后得出的准确率也是不一样的
# 具体其他参数可以查看sklearn官方文档的API

# 使用多分类的算法,将多分类问题转化成了多个二分类问题
log_reg = LogisticRegression(multi_class='ovr',solver='sag',random_state=0)

log_reg.fit(X,Y)

X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
# print(X_new)

# predict_proba返回的是一个n行k列的数值,第i行第j列上的数值是模型预测第i个预测样本为某个标签的概率并且每一行的概率和为1
# 比较的概率当哪个概率最大将会取哪一个类别
y_proba = log_reg.predict_proba(X_new)
print(y_proba)

print(y_proba[0][0],y_proba[0][1],y_proba[0][2],y_proba[0][0]+y_proba[0][1]+y_proba[0][2])
# 预测新数据的列别
y_hat = log_reg.predict(X_new)
# print(y_hat)

# 打印各个权值,由于为3分类问题,将其分成了3个二分类问题,因此将有3组w参数,每一组对应着一个二分类模型
print(log_reg.coef_)
# 将有3个偏置值,每一个对应着一个二分类模型
print(log_reg.intercept_)

plt.plot(X_new, y_proba[:, 2], 'g-', label='Iris-Virginica')
plt.plot(X_new, y_proba[:, 1], 'r-', label='Iris-Versicolour')
plt.plot(X_new, y_proba[:, 0], 'b--', label='Iris-Setosa')

plt.show()

'''

"""
# 示例2:逻辑回归,多分类,并有4个特征值
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

X = iris['data']
print(X)

# 获取标签数据,分类的列别
Y = iris['target']
# print(Y)

# 创建逻辑回归的实例,该实例不仅仅能进行二分类的问题,还能进行多分类的问题
# max_iter: 最大迭代次数，这个是硬限制，它的优先级要高于tol参数，不论训练的标准和精度达到要求没有，都要停止训练。默认值是-1，指没有最大次数限制
# tol:残差收敛条件，默认是0.0001，也就是只需要收敛的时候两步只差＜0.0001就停止，可以设置更大或更小。(逻辑回归模型的损失函数是残差平方和)
# C:正则化系数，正则化强度的导数，必须是一个正数，值越小，正则化强度越大，即防止过拟合的程度更大
# random_state:随机种子的设置，默认是None,如果设置了随机种子，那么每次使用的训练集和测试集都是一样的，这样不管你运行多少次，最后的准确率都是一样的；如果没有设置，那么每次都是不同的训练集和测试集，最后得出的准确率也是不一样的
# 具体其他参数可以查看sklearn官方文档的API

# 使用多分类的算法,将多分类问题转化成了多个二分类问题
log_reg = LogisticRegression(multi_class='ovr',solver='sag',random_state=0)

log_reg.fit(X,Y)

X_new = np.linspace(0, 3, 1000).reshape(-1, 4)
# print(X_new)

# predict_proba返回的是一个n行k列的数值,第i行第j列上的数值是模型预测第i个预测样本为某个标签的概率并且每一行的概率和为1
# 比较的概率当哪个概率最大将会取哪一个类别
y_proba = log_reg.predict_proba(X_new)
print(y_proba)

# print(y_proba[0][0],y_proba[0][1],y_proba[0][2],y_proba[0][0]+y_proba[0][1]+y_proba[0][2])
# 预测新数据的列别
y_hat = log_reg.predict(X_new)
# print(y_hat)

# 打印各个权值,由于为3分类问题,将其分成了3个二分类问题,因此将有3组w参数,每一组对应着一个二分类模型
print(log_reg.coef_)
# 将有3个偏置值,每一个对应着一个二分类模型
print(log_reg.intercept_)

"""

# 示例3:使用softmax算法进行分类
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

X = iris['data']
print(X)

# 获取标签数据,分类的列别
Y = iris['target']
# print(Y)

# 创建逻辑回归的实例,该实例不仅仅能进行二分类的问题,还能进行多分类的问题
# max_iter: 最大迭代次数，这个是硬限制，它的优先级要高于tol参数，不论训练的标准和精度达到要求没有，都要停止训练。默认值是-1，指没有最大次数限制
# tol:残差收敛条件，默认是0.0001，也就是只需要收敛的时候两步只差＜0.0001就停止，可以设置更大或更小。(逻辑回归模型的损失函数是残差平方和)
# C:正则化系数，正则化强度的导数，必须是一个正数，值越小，正则化强度越大，即防止过拟合的程度更大
# random_state:随机种子的设置，默认是None,如果设置了随机种子，那么每次使用的训练集和测试集都是一样的，这样不管你运行多少次，最后的准确率都是一样的；如果没有设置，那么每次都是不同的训练集和测试集，最后得出的准确率也是不一样的
# 具体其他参数可以查看sklearn官方文档的API

# 使用多分类的算法,将多分类问题转化成了多个二分类问题
# multi_class='multinomial':使用softmax算法
log_reg = LogisticRegression(multi_class='multinomial',solver='sag',random_state=0)

log_reg.fit(X,Y)

X_new = np.linspace(0, 3, 1000).reshape(-1, 4)
# print(X_new)

# predict_proba返回的是一个n行k列的数值,第i行第j列上的数值是模型预测第i个预测样本为某个标签的概率并且每一行的概率和为1
# 比较的概率当哪个概率最大将会取哪一个类别
y_proba = log_reg.predict_proba(X_new)
print(y_proba)

# print(y_proba[0][0],y_proba[0][1],y_proba[0][2],y_proba[0][0]+y_proba[0][1]+y_proba[0][2])
# 预测新数据的列别
y_hat = log_reg.predict(X_new)
# print(y_hat)

# 打印各个权值,由于为3分类问题,将其分成了3个二分类问题,因此将有3组w参数,每一组对应着一个二分类模型
print(log_reg.coef_)
# 将有3个偏置值,每一个对应着一个二分类模型
print(log_reg.intercept_)