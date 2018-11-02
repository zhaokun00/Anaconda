
from sklearn.feature_extraction import  DictVectorizer

from sklearn.preprocessing import StandardScaler

#  示例1:字典数据特征抽取

def dicFunction() :
    # 定义字典类型数据
    map1 = {'city':'北京','temp':'20'}
    map2 = {'city':'上海','temp':'30'}
    map3 = {'city':'广州','temp':'40'}

    # 定义列表数据
    data = [map1,map2,map3]

    # print(data)

    dic = DictVectorizer(sparse=False)

    d = dic.fit_transform(data)

    # 获取特征的名字
    print(dic.get_feature_names())

    print(d)

# 示例2:测试fit、transform、fit_transform之间的区别
def fitFunction() :

    data = [[1,2,3],[4,5,6]]

    s = StandardScaler()

    # print(s.fit_transform(data))
    #
    # ss = StandardScaler()
    #
    # print(ss.fit(data))
    #
    # print(ss.transform(data))

    print(s.transform(data))


if __name__ == "__main__":

    fitFunction()