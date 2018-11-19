import sklearn.datasets as skdata
from sklearn.model_selection import train_test_split
import numpy as np

'''
API介绍:
datasets.load_*:获取小规模数据集,数据集包含在datasets中
darasets.fetch_*(data_home=None):获取大规模数据集,需要从网络上下载,函数的第一个参数是data_home,
表示数据集下载目录,默认是~/scikit_learn_data,例如windows系统C:/Users/Administrator/scikit_learn_data

load*和fetch*返回的数据类型是datasets.base.Bunch(字典格式)

字典数据中的属性值:
data:特征数据数组,是[n_sample * n_feature]的二维numpy.ndarray数组
target:标签数组,是n_sample的一维numpy.ndarray数组
DESCR:数据描述
feature_names:特征名,回归数据集没有
target_names:标签名,回归数据集没有

'''
data = skdata.load_iris()

# print("type:",type(data))

# 遍历字典数据,遍历key值与value值
# for key in data:
#     print(key,data[key])

# print(data)

# print("type:",type(data))
# print("data:",data.data)
# print("DESCR:",data.DESCR)
# print("target:",data.target)

print("data形状:",np.shape(data["data"]))
print("target形状:",np.shape(data["target"]))

'''
数据集分割函数:
x:数据集的特征值
y:数据集的标签值
test_size:测试集的大小,一般为float类型,数据集按照该比例进行切分训练集与测试集
random_state:随机数种子,不同的种子会造成不同的随机采样结果,相同的种子采样结果相同
return:训练集特征值、测试集特征值、训练集标签值、测试集标签值
'''
x_train,x_test,y_train,y_test = train_test_split(data["data"],data["target"],test_size=0.25)

print("x_train形状:",np.shape(x_train))
print("x_test形状:",np.shape(x_test))
print("y_train形状:",np.shape(y_train))
print("y_test形状:",np.shape(y_test))


'''
获取大规模数据

subset:train、test、all可选,选择要加载的数据集,训练集、测试集、还是全部
'''
data = skdata.fetch_20newsgroups()

# print("type:",type(data))
# print("data:",data.data)
# print("DESCR:",data.DESCR)
# print("target:",data.target)

for key in data:
    print(key)

print(data['data'][0])
print(data['target'][0])