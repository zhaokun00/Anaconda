import numpy as np
from numpy import float64
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


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

def knn():

    x_train = [[101,10],[99,5],[98,2],[3,104],[2,100],[1,81]]

    y_train = [1,1,1,2,2,2]

    # print(x_train)
    # print(y_train)
#
#     '''
#     python3.5的numpy设置array为float64，报错"name float64 is not defined"
#     '''
    x_train = np.array(x_train,dtype=float64)
    y_train = np.array(y_train)
#
    scaler = StandardScaler()
#
#     # 对训练数据进行标准化,使用了训练数据的标准化的实例
    x_train = scaler.fit_transform(x_train)

    print(x_train)
    print(y_train)
#
#     '''
#     n_neighbors:邻居数
#     '''
    knn = KNeighborsClassifier(n_neighbors=3)

    knn.fit(x_train,y_train)

    x_test = [[300,1],[4,100],[300,2]]
#
#     # 对测试数据进行标准化,使用前面的标准化的实例
    x_test = scaler.transform(x_test)
    y_test = [1,2,1]
#
#     # 对其进行预测
    result = knn.predict(x_test)
#
#     # 计算准确率(预测结果正确地百分比),用于模型的评估
    score = knn.score(x_test,y_test)
#
    print(result)
    # print(score)
    targetName = ["类别1","类别2"]
    print("精确率与召回率:",classification_report(y_test,result,target_names=targetName))

if __name__ == "__main__":

    knn()