import numpy as np
from numpy import float64
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

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

# 交叉验证与网格搜索
'''
交叉验证与网格搜索的目的:选取最优的超参数
交叉验证:
    将拿到的数据分为训练和验证集.例如将数据分为5份,其中一份作为验证集,然后经过5次的测试(假如有1个超参数,超参数有
    2个取值,则要进行5*2次测试,获取最终的2个平均值,假如有2个超参数a、b,其中a有n种取值,b有m种取值,则要进行5*n*m次测试,
    取n*m种结果,从中选取最优的一组超参数),每次都更换验证集,即得到5组模型的结果,取平均值最为最终的结果,又称为5折交叉验证
    
超参数搜索-网格搜索
    通常情况下,有很多参数都是需要手动指定的,这种叫做超参数,但是手动过程繁杂,所以需要对模型预设几种超参数组合,每组超参数
    都采用交叉验证来进行评估,最后选出最优参数组合建立模型
    
    
def __init__(self, estimator, param_grid, scoring=None, fit_params=None,
         n_jobs=1, iid=True, refit=True, cv=None, verbose=0,
         pre_dispatch='2*n_jobs', error_score='raise',
         return_train_score=True):
    
    参数:             
    estimator:估计器对象
    param_grid:估计器参数,为map类型
    cv:指定几折交叉验证
    
    方法:
    fit:训练数据
    score:准确率
    
'''
def knnCross():
    x_train = [[101, 10], [99, 5], [98, 2], [3, 104], [2, 100], [1, 81]]

    y_train = [1, 1, 1, 2, 2, 2]

    x_train = np.array(x_train, dtype=float64)
    y_train = np.array(y_train)

    scaler = StandardScaler()

    x_train = scaler.fit_transform(x_train)

    knn = KNeighborsClassifier()

    x_test = [[300, 1], [4, 100], [300, 2]]

    x_test = scaler.transform(x_test)

    print(x_test)
    y_test = [1, 2, 1]

    param = {"n_neighbors": [1,2]}

    search = GridSearchCV(knn,param,cv=2)

    search.fit(x_train, y_train)

    # result = search.predict(x_test)
    #
    # print(result)

    # 交叉验证中最好的估计器模型
    print(search.best_estimator_)
    # 交叉验证中最好的一组参数
    print(search.best_params_)
    # 在交叉验证中测试最好的结果
    print(search.best_score_)
    print(search.cv_results_)

if __name__ == "__main__":

    # knn()
    knnCross()