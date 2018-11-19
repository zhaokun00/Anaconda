from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
import numpy as np

# 示例1:删除所有低方差特征
'''
VarianceThreshold,训练集差异低于threshold的特征将被删除,默认值是保留所有非零方差特性,即
删除所有样本中具有相同值的特征
'''
def var():
    data = [[8, 2], [3, 4]]

    data = np.array(data)

    o = np.var(data, axis=0)

    print(o)

    scaler = VarianceThreshold(threshold=1.0)

    data = scaler.fit_transform(data)

    print(data)

def pca():

    # data = [[1, 2, 3], [1, 2, 6]]
    data = [[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]]

    data = np.array(data)

    scaler = PCA(n_components=0.99)

    data = scaler.fit_transform(data)

    print(data)
if __name__ == "__main__":

    # var()

    pca()