import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import OneHotEncoder

# 示例1:归一化操作
def minmax():

    # data = np.array([[1,2,3],[2,3,4]])
    data = [[1,2,3],[2,3,4],[5,8,4]]

    print("type:",type(data))
    print(data)

    # 通过参数dtype,将int32类型的数据转换成float类型
    data = np.array(data,dtype=np.float)

    print("type:", type(data))
    print(data)

    # 参数feature_range指定归一化后的最小值和最大值
    scaler = MinMaxScaler(feature_range=(1,2))

    # 进行数据转换
    data = scaler.fit_transform(data)

    print(data)

# 示例2:标准化操作
def stand():

    data = [[8,2],[3,4]]

    data = np.array(data)

    print(data)
    print(data.shape)
    print("平均值=",data.mean(axis=0))
    print("标准差=",data.std(axis=0))
    print("方差=", data.var(axis=0))

    print((data -data.mean(axis=0))/data.std(axis=0))

    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    print(data)
    print(data.shape)
    print(type(data))

    print("平均值=",data.mean(axis=0))
    print("标准差=",data.std(axis=0))
    print("方差=", data.var(axis=0))

# 示例3:缺失值操作
'''
缺失值的处理办法
1.删除:如果每列或者行数据缺失值达到一定的比例,建议放弃整列或者整行
2.插补:可以通过缺失值每行或者每列的平均值、中位数来填充
'''
def miss():

    data = [[np.nan,2],[3,4],[1,2]]

    data = np.array(data)

    print(data)

    # 参数missing_values:数据为空,strategy:采用平均值进行补充
    scaler = Imputer(missing_values="NaN", strategy="mean")

    data = scaler.fit_transform(data)

    print(data)

def oneHot():
    data = np.array([[0, 1, 5], [1, 2, 3], [0, 1, 6]])

    '''
    参数:categorical_features是需要独立热编码的列索引,n_values是对应categorical_features中各类别的种类

    两种编码的格式:自然编码和独立热编码
    自然状态码为：000,001,010,011,100,101
    独立热编码为：000001,000010,000100,001000,010000,100000
    '''
    # 第0列对应着第一个特征有0,1这两个类别,第二个有1,2这两个类别,第三个有5,3,6这3个类别
    encoder = OneHotEncoder(sparse=False, categorical_features=[0, 1])

    d = encoder.fit_transform(data)

    # print(encoder.get_params())
    #
    # print(encoder.categorical_features)

    print(d)

# 示例2:计算协方差
def cov():
    data = [[1,2],[3,4]]

    data = np.array(data)

    print(data)

    print(np.mean(data,axis=0))
    print(np.var(data,axis=0))

    # 计算协方差
    '''
    rowvar:布尔值,默认为True,True:行是特征,列是样本
                            False:样本,列是特征
    bias:布尔值,默认是False,False:无偏估计,协方差计算分母为n-1
                           True:有偏估计,协方差计算分母为n(n为样本数)
    '''
    print(np.cov(data,rowvar=False,bias=True))


if __name__ == "__main__":

    # minmax()

    # stand()

    miss()
    # minmax()

    cov()