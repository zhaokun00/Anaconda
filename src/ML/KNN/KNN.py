import numpy as np
from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pandas as pd
# from numpy import float64
# import os
# os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
#
#

# https://blog.csdn.net/imstudying/article/details/77876159
# https://blog.csdn.net/zhu1365377615/article/details/80320687
# https://blog.csdn.net/zhuiyuanzhongjia/article/details/80170412
# def knn():
#
#     '''
#     在sklean中,估计器(estimator)是一个重要的角色,分类器和回归器都属于estimator,是一类实现了算法的API
#     用于分类的估计器:
#         sklean.neighbors - k近邻算法
#         skelan.naive_bayes - 贝叶斯
#         sklean.linear_model.LogisticRefression - 逻辑回归
#     用于回归的估计器:
#         sklean.linear_model.LinearRegression - 线性回归
#         sklean.libear_model.Ridge - 岭回归
#     '''
#     # https://www.cnblogs.com/erbaodabao0611/p/7588840.html
#     x_train = [[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]]
#
#     y_train = [0,0,0,1,1,1]
#
#     # print(x_train)
#     # print(y_train)
#
#     '''
#     python3.5的numpy设置array为float64，报错"name float64 is not defined"
#     '''
#     x_train = np.array(x_train,dtype=float64)
#     y_train = np.array(y_train)
#
#     scaler = StandardScaler()
#
#     # 对训练数据进行标准化,使用了训练数据的标准化的实例
#     x_train = scaler.fit_transform(x_train)
#
#     print(x_train)
#     print(y_train)
#
#     '''
#     n_neighbors:邻居数
#     '''
#     knn = KNeighborsClassifier(n_neighbors=3)
#
#     knn.fit(x_train,y_train)
#
#     x_test = [[4,100]]
#
#     # 对测试数据进行标准化,使用前面的标准化的实例
#     x_test = scaler.transform(x_test)
#     y_test = [0]
#
#     # 对其进行预测
#     result = knn.predict(x_test)
#
#     # 计算准确率(预测结果正确地百分比),用于模型的评估
#     score = knn.score(x_test,y_test)
#
    # print(result)
    # print(score)
    #
    # print("精确率与召回率:",classification_report(y_test,result))

def naviebayes():
    """
    朴素贝叶斯进行文本分类
    :return: None
    """
    news = fetch_20newsgroups(subset='all')

    # print(np.shape(news))


    # print(news)
    # 进行数据分割
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25,random_state=1)

    print(np.shape(x_test))
    print(np.shape(y_test))

    # print(x_test[0])

    print("***************************************")
    print(np.shape(y_train))
    print(np.shape(y_test))
    print(np.shape(news['target']))
    print(news['target'])

    print(np.min(y_test))
    print(np.max(y_test))
    print(news.target_names)

    for it in news.target_names:
        print(it)
    '''
    # 对数据集进行特征抽取
    tf = TfidfVectorizer()

    # 以训练集当中的词的列表进行每篇文章重要性统计['a','b','c','d']
    x_train = tf.fit_transform(x_train)

    print(tf.get_feature_names())

    x_test = tf.transform(x_test)

    # 进行朴素贝叶斯算法的预测
    mlt = MultinomialNB(alpha=1.0)

    # print(x_train.toarray())

    mlt.fit(x_train, y_train)

    y_predict = mlt.predict(x_test)
    #
    print("预测的文章类别为：", y_predict)
    #
    # # 得出准确率
    print("准确率为：", mlt.score(x_test, y_test))
    #
    print("每个类别的精确率和召回率：", classification_report(y_test, y_predict, target_names=news.target_names))
'''
if __name__ == "__main__":

    naviebayes()