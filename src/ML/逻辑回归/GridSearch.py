import numpy as np
from sklearn import datasets
from sklearn.linear_model import  LogisticRegression
import  matplotlib.pyplot as plt
from time import time
from sklearn.model_selection import GridSearchCV


def report(results, n_top=3):
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        print(candidates)
        print("------------")
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            # 打印最好的平均分数,方差值
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                  results['mean_test_score'][candidate],
                  results['std_test_score'][candidate]))
            # 打印参数
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")

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

start = time()

# print("start time:",start)

# 使用多分类的算法,将多分类问题转化成了多个二分类问题
log_reg = LogisticRegression(multi_class='ovr',solver='sag',random_state=0)

# 定义网格搜索的参数
param_grid = {
    "tol":[1e-4, 1e-3, 1e-2],
    "C":[0.4, 0.6, 0.8]
}

# 定义网格搜索的实例
# param_grid：值为字典或者列表，即需要最优化的参数的取值，param_grid =param_test1，param_test1 = {'n_estimators':range(10,71,10)}
# cv :交叉验证参数，默认None，使用三折交叉验证。指定fold数量，默认为3，也可以是yield训练/测试数据的生成器,将原本的训练数据分成几份
grid_search = GridSearchCV(log_reg,param_grid=param_grid,cv=3)

grid_search.fit(X,Y)

print("GridSearchCV took %.2f seconds for %d candidate parameter settings."
      % (time() - start, len(grid_search.cv_results_['params'])))

print(grid_search.cv_results_)
report(grid_search.cv_results_)


# print("最好的得分:",grid_search.best_score_)
#
# 最好的参数
# print(grid_search.best_params_)
#
# print(grid_search.grid_scores_)

X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
# print(X_new)

# predict_proba返回的是一个n行k列的数值,第i行第j列上的数值是模型预测第i个预测样本为某个标签的概率并且每一行的概率和为1
# 比较的概率当哪个概率最大将会取哪一个类别
y_proba = grid_search.predict_proba(X_new)

print(y_proba)

print(grid_search.estimator)

print(grid_search.best_estimator_)

# 打印各个权值,由于为3分类问题,将其分成了3个二分类问题,因此将有3组w参数,每一组对应着一个二分类模型
print(log_reg.coef_)
# 将有3个偏置值,每一个对应着一个二分类模型
print(log_reg.intercept_)

#
# print(y_proba[0][0],y_proba[0][1],y_proba[0][2],y_proba[0][0]+y_proba[0][1]+y_proba[0][2])
# 预测新数据的列别
y_hat = grid_search.predict(X_new)
# print(y_hat)

plt.plot(X_new, y_proba[:, 2], 'g-', label='Iris-Virginica')
plt.plot(X_new, y_proba[:, 1], 'r-', label='Iris-Versicolour')
plt.plot(X_new, y_proba[:, 0], 'b--', label='Iris-Setosa')

plt.show()
