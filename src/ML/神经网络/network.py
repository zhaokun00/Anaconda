# https://blog.csdn.net/Mrzhang0419/article/details/79519994
# 多层感知机的分类问题包
from sklearn.neural_network import MLPClassifier
# 多层感知机的回归问题包
from sklearn.neural_network import MLPRegressor

import numpy as np


# X = [[0.05, 0.1]]
# y = [[0.01,0.99]]


# 示例1:使用神经网络进行分类问题

"""
# 训练样本
# 有两个训练样本,有两个维度
X = [[0., 0.], [1., 1.]]
# 标签有0和1两个分类,[0.,0.]标签值为0,[1.,1.]标签值为1
y = [0, 0]

# 创建多层感知机的示例
#
clf = MLPClassifier(solver='sgd', alpha=1e-5, activation='logistic',
                    hidden_layer_sizes=(2,3,2), max_iter=2000, tol=1e-4)
# 训练数据
clf.fit(X, y)

# 获取各个权重参数,即w,各个层次的w值
ws = clf.coefs_
# print(clf.coefs_)

print('---------')

# 打印权重w的形状
for w in ws:
    print("w:",w)
    print("shape:",w.shape)

# print([coef.shape for coef in clf.coefs_])
# print([coef for coef in clf.coefs_])

# 打印概率值
predicted_proba = clf.predict_proba([[0., 0.]])
print("proba:",predicted_proba)

# 打印最终的分类结果
predicted_value = clf.predict([[0., 0.]])
print("value:",predicted_value)
"""

# 示例2:神经网络的回归问题
X = [[0.05, 0.1]]
Y = [[0.01,0.99]]

# 创建多层感知机的示例
"""
1. hidden_layer_sizes :隐藏层中每个隐藏层中的节点数
2. activation :{‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, 默认‘relu 
- ‘identity’： no-op activation, useful to implement linear bottleneck， 
返回f(x) = x 
- ‘logistic’：the logistic sigmoid function, returns f(x) = 1 / (1 + exp(-x)). 
- ‘tanh’：the hyperbolic tan function, returns f(x) = tanh(x). 
- ‘relu’：the rectified linear unit function, returns f(x) = max(0, x) 
4. solver： {‘lbfgs’, ‘sgd’, ‘adam’}, 默认 ‘adam’，用来优化权重 
- lbfgs：quasi-Newton方法的优化器 
- sgd：随机梯度下降 
- adam： Kingma, Diederik, and Jimmy Ba提出的机遇随机梯度的优化器 
注意：默认solver ‘adam’在相对较大的数据集上效果比较好（几千个样本或者更多），对小数据集来说，lbfgs收敛更快效果也更好。 
5. alpha :float,可选的，默认0.0001,正则化项参数 
6. batch_size : int , 可选的，默认‘auto’,随机优化的minibatches的大小，如果solver是‘lbfgs’，分类器将不使用minibatch，当设置成‘auto’，batch_size=min(200,n_samples) 
7. learning_rate :{‘constant’，‘invscaling’, ‘adaptive’},默认‘constant’，用于权重更新，只有当solver为’sgd‘时使用 
- ‘constant’: 有‘learning_rate_init’给定的恒定学习率 
- ‘incscaling’：随着时间t使用’power_t’的逆标度指数不断降低学习率learning_rate_ ，effective_learning_rate = learning_rate_init / pow(t, power_t) 
- ‘adaptive’：只要训练损耗在下降，就保持学习率为’learning_rate_init’不变，当连续两次不能降低训练损耗或验证分数停止升高至少tol时，将当前学习率除以5. 
8. max_iter: int，可选，默认200，最大迭代次数。 
9. random_state:int 或RandomState，可选，默认None，随机数生成器的状态或种子。 
10. shuffle: bool，可选，默认True,只有当solver=’sgd’或者‘adam’时使用，判断是否在每次迭代时对样本进行清洗。 
11. tol：float, 可选，默认1e-4，优化的容忍度 
12. learning_rate_int:double,可选，默认0.001，初始学习率，控制更新权重的补偿，只有当solver=’sgd’ 或’adam’时使用。 
13. power_t: double, optional, default 0.5，只有solver=’sgd’时使用，是逆扩展学习率的指数.当learning_rate=’invscaling’，用来更新有效学习率。 
14. verbose : bool, optional, default False,是否将过程打印到stdout 
15. warm_start : bool, optional, default False,当设置成True，使用之前的解决方法作为初始拟合，否则释放之前的解决方法。 
16. momentum : float, default 0.9,Momentum(动量） for gradient descent update. Should be between 0 and 1. Only used when solver=’sgd’. 
17. nesterovs_momentum : boolean, default True, Whether to use Nesterov’s momentum. Only used when solver=’sgd’ and momentum > 0. 
18. early_stopping : bool, default False,Only effective when solver=’sgd’ or ‘adam’,判断当验证效果不再改善的时候是否终止训练，当为True时，自动选出10%的训练数据用于验证并在两步连续爹迭代改善低于tol时终止训练。 
19. validation_fraction : float, optional, default 0.1,用作早期停止验证的预留训练数据集的比例，早0-1之间，只当early_stopping=True有用 
20. beta_1 : float, optional, default 0.9，Only used when solver=’adam’，估计一阶矩向量的指数衰减速率，[0,1)之间 
21. beta_2 : float, optional, default 0.999,Only used when solver=’adam’估计二阶矩向量的指数衰减速率[0,1)之间 
22. epsilon : float, optional, default 1e-8,Only used when solver=’adam’数值稳定值。 
属性说明： 
- classes_:每个输出的类标签 
- loss_:损失函数计算出来的当前损失值 
- coefs_:列表中的第i个元素表示i层的权重矩阵 
- intercepts_:列表中第i个元素代表i+1层的偏差向量 
- n_iter_ ：迭代次数 
- n_layers_:层数 
- n_outputs_:输出的个数 
- out_activation_:输出激活函数的名称。 
方法说明： 
- fit(X,y):拟合 
- get_params([deep]):获取参数 
- predict(X):使用MLP进行预测 
- predic_log_proba(X):返回对数概率估计 
- predic_proba(X)：概率估计 
- score(X,y[,sample_weight]):返回给定测试数据和标签上的平均准确度 
- set_params(**params):设置参数。
"""
clf = MLPRegressor(solver='sgd', alpha=1e-5,activation='logistic',
                    hidden_layer_sizes=(2,), max_iter=100000, tol=1e-4,random_state=0)
# 训练数据
clf.fit(X, Y)

ws = clf.coefs_

for w in ws:
    print("w:",w)
    print("shape:",w.shape)

vaule = clf.predict([0.05, 0.1])

print("vaule",vaule)

#

# X = 2 * np.random.rand(100, 1)
#
# bias = np.random.randn(100, 1)
#
# Y = 4 + 3 * X + bias
#
# clf = MLPClassifier(solver='sgd', alpha=1e-5, activation='logistic',
#                     hidden_layer_sizes=(2, 1), max_iter=2000, tol=1e-4)
# clf.fit(X, Y)

# x = [[0.]]
#
# print(clf.predict(x))