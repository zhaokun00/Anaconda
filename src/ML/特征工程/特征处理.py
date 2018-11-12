import numpy as np
from sklearn.preprocessing import MinMaxScaler

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

if __name__ == "__main__":

    minmax()