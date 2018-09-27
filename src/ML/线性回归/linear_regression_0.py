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
y = 4 + 3 * X + np.random.randn(100, 1)

print(y)
# 整合X0和X1
X_b = np.c_[np.ones((100, 1)), X]
print(X_b)

# 常规等式求解theta
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print(theta_best)

# 创建测试集里面的X1
X_new = np.array([[0], [2]])
X_new_b = np.c_[(np.ones((2, 1))), X_new]
print(X_new_b)
y_predict = X_new_b.dot(theta_best)
print(y_predict)

plt.plot(X_new, y_predict, 'r-')
plt.plot(X, y, 'b.')
plt.axis([0, 2, 0, 15])
plt.show()

X_new = np.array([[0], [2]])

print(X_new)

'''
用vnc实现Windows远程连接linux桌面之服务器配置
https://www.jb51.net/article/93758.htm

机器学习各个算法示例
https://www.cnblogs.com/hemiy/p/6155425.html

线性回归:
http://wiki.mbalib.com/wiki/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92%E9%A2%84%E6%B5%8B%E6%B3%95
https://www.cnblogs.com/lliuye/p/9120839.html
https://www.cnblogs.com/futurehau/p/6105011.html

梯度下降
https://www.cnblogs.com/pinard/p/5970503.html

导数、极值点、驻点、
https://www.cnblogs.com/Kaivenblog/p/6542095.html

https://blog.csdn.net/xueyingxue001/article/details/51858037
凸函数、凹函数

逻辑回归
https://blog.csdn.net/suipingsp/article/details/41822313
https://blog.csdn.net/zj360202/article/details/78688070

神经网络
https://www.cnblogs.com/subconscious/p/5058741.html

决策树
https://www.cnblogs.com/xinbaby829/p/7003422.html

逻辑回归、决策树、支持向量机的区别
http://www.sohu.com/a/192696017_99950807

支持向量机
https://blog.csdn.net/v_july_v/article/details/7624837/
https://www.cnblogs.com/luyaoblog/p/6775342.html

BP神经网络
http://www.cnblogs.com/charlotte77/p/5629865.html
https://www.cnblogs.com/biaoyu/archive/2015/06/20/4591304.html

pycharm 中编辑python文本中间出现有一条分割线, 怎样去掉
https://bbs.csdn.net/topics/392189677

pycharm激活码
https://blog.csdn.net/u014044812/article/details/78727496

python环境搭建
https://blog.csdn.net/qq_29883591/article/details/52664478/

pycharm新建项目
https://www.cnblogs.com/loyung/p/8554836.html

pycharm 报错：pycharm please specify a different SDK name
https://blog.csdn.net/wu_l_v/article/details/79049718

一分钟实现内网穿透（ngrok服务器搭建）
https://blog.csdn.net/zhangguo5/article/details/77848658?utm_source=5ibc.net&utm_medium=referral

Go 交叉编译
https://blog.csdn.net/xingwangc2014/article/details/65013892

ubuntu 默认防火墙安装、启用、查看状态
https://www.cnblogs.com/OnlyDreams/p/7210914.html

linux上搭建ngrok服务端以及编译客户端，及相关防火墙配置
https://blog.csdn.net/qq_36798753/article/details/72958823

Pycharm更换pip源为国内
https://www.cnblogs.com/hkgov/p/7799078.html
'''