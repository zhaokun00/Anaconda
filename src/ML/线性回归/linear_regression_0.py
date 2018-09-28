import numpy as np
import matplotlib.pyplot as plt

# https://blog.csdn.net/u010758410/article/details/71799142
# https://blog.csdn.net/yj1556492839/article/details/79031693
# https://blog.csdn.net/lanchunhui/article/details/51004387
# https://www.cnblogs.com/zhizhan/p/5615947.html
__author__ = 'yasaka'

"""
numpy中有一些常用的用来产生随机数的函数,randn()和rand()就属于其中
np.random.random(size)生成[0.1)之间的浮点数,size是浮点数的个数
np.random.rand(d0,d1,...,dn)的随机样本为[0,1)中,dn表示维度
np.random.randn(d0,d1,...,dn)是从标准正太分布中返回一个或多个样本值

"""
# 产生2个[0,1)之间的随机数
# x1 = np.random.random(2)
# ndarray数据结构就相当于矩阵的形式,有1维的矩阵、2维的矩阵...n维的矩阵
# print(x1,type(x1))

# 产生一个2X2的矩阵即2行2列,数值在[0,1)之间
# x1 = np.random.rand(2,2)
# print(x1,type(x1))

# 产生一个2X3的矩阵即2行3列,数值可正可负
# x1 = np.random.randn(2,3)
# print(x1,type(x1))

# randint(low, high=None, size=None, dtype='l')
# 返回随机整数，范围区间为[low,high），包含low，不包含high
# 参数：low为最小值，high为最大值，size为数组维度大小，dtype为数据类型，默认的数据类型是np.int
# high没有填写时，默认生成随机数的范围是[0，low)
# x1 = np.random.randint(1,100,10)
# print(x1)

# 产生一个100X1的矩阵即100行1列,数值在[0,1)之间
X = 2 * np.random.rand(100, 1)

print("X取值:")
# print(X)


# 随机生成的偏移量也是100X1的数据
bias = np.random.randn(100, 1)
print("bias取值:")
# print(bias)

# X与Y之间的真实关系,产生的Y是100X1的矩阵,即100行1列的数据,由于随机加上了偏移值,因此X与Y之间的关系并不是直线关系
Y = 4 + 3 * X + bias
print("y的取值")
# print(Y)

plt.plot(X, Y, 'b.')
plt.show()
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

# X_new = np.array([[0], [2]])
#
#
# print(X_new)

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