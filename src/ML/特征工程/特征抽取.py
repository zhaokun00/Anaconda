import numpy as np

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer,TfidfTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

import jieba

'''
特征抽取:
    1.针对非连续型数据
    2.针对文本进行特征值化
'''
#  示例1:字典数据特征抽取

def dicFunction() :

    # 定义字典类型数据,实际上就是键值对的形式
    map1 = {'city':'北京','temp':'20'}
    map2 = {'city':'上海','temp':'30'}
    map3 = {'city':'广州','temp':'40'}

    # 定义列表数据,用字典数据组成
    data = [map1,map2,map3]

    # 输出形式:[{'city': '北京', 'temp': '20'}, {'city': '上海', 'temp': '30'}, {'city': '广州', 'temp': '40'}]
    # print(data)

    # 定义字典数据抽取器
    # 参数:sparse:结果是否使用sparse形式表示,一般情况下为False,返回值更加直观
    dic = DictVectorizer(sparse=False)

    # dic.fit(data)
    # d = dic.transform(data)

    # 相当于fit与transform两个函数的结合体,将原本的数据转换了one-hot编码的形式
    # 转换了一个二维数组的形式,为ndarray类型
    d = dic.fit_transform(data)

    # 类型为ndarray类型
    # print("type",type(d))

    # 获取特征的名字
    print(dic.get_feature_names())

    print(d)

    # 返回原来的数据
    # print(dic.inverse_transform(d))

# 示例2:测试fit、transform、fit_transform之间的区别
'''
   fit(x,y)传2个参数是有监督学习的算法
   fit(x)传入一个参数是无监督学习的算法,比如降维、特征提取、标准化等

   fit和transform没有任何关系,仅仅是数据处理的两个不同的环节,之所以出来这个函数,仅仅是为了写代码方便,
   所以会发现transform()和fit_transform()的运行结果是一样的

   注意:运行结果一样不代表这两个函数可以相互替换,解释如下:
   sklearn里面封装好的各种算法都要fit,然后才能调用各种API函数,transform()函数只是其中的一个API方法,所以当你调用
   除transform()之外的方法,必须先要fit,为了通用的写代码.还是分开写比较好
'''
def fitFunction() :

    data = [[1,2,3],[4,5,6]]

    print(np.mean(data,axis=0))
    print(np.std(data,axis=0))
    print((data-np.mean(data,axis=0))/np.std(data,axis=0))

    # 定义标准化实例
    s = StandardScaler()

    # 在fit()函数中会计算一些均值,方差之列的参数
    print(s.fit(data))

    # 在transform()函数中进行数据转换,会使用前面fit计算的参数进行转换
    print(s.transform(data))

    test_data = [[7,8,9]]

    print((test_data-np.mean(data,axis=0))/np.std(data,axis=0))
    print(s.transform(test_data))

    ss = StandardScaler()

    print(ss.fit_transform(test_data))
    # 相当于前面两个函数的结合体
    # print(s.fit_transform(data))

# 示例3:OneHotEncoder:独立热编码
'''
在分类和聚类运算中,我们经常计算两个个体之间的距离,对于连续型的数字(Numric)这一点不成问题,但对于名词性(Norminal)
的类别,计算距离很难,即使将类别与数字对应,例如{A,B,C}与[0,1,2]对应我们也不能认为A与B,B与C距离为1,A与C距离为2,
独立热编码正是为了处理这种距离的度量,该方法认为每个类别之间的距离是一样的,该方法将类别与向量对应,例如{A,B,C}分布与
[1,0,0],[0,1,0],[0,0,1]对应,注意现在各个类别之间的欧氏距离是相同的

'''
def oneHot():

    data = np.array([[0,1,5],[1,2,3],[0,1,6]])

    '''
    参数:categorical_features是需要独立热编码的列索引,n_values是对应categorical_features中各类别的种类
    
    两种编码的格式:自然编码和独立热编码
    自然状态码为：000,001,010,011,100,101
    独立热编码为：000001,000010,000100,001000,010000,100000
    '''
    # 第0列对应着第一个特征有0,1这两个类别,第二个有1,2这两个类别,第三个有5,3,6这3个类别
    encoder = OneHotEncoder(sparse=False,categorical_features=[0,1])

    d = encoder.fit_transform(data)

    # print(encoder.get_params())
    #
    # print(encoder.categorical_features)

    print(d)

# 示例4:对文本进行特征抽取
def countVecor():

    # 对单词统计出现的次数,只是单纯的统计单词的出现的次数
    cv = CountVectorizer()

    # 对英文进行分词,组成的为list类型数据,每一条list数据为一个样本,一条样本由多个单词组成,单词与单词之间使用空格来区分的
    # 如果一条样本中某个单词出现多次,将来矩阵中数值为多个,不会统计单个字母
    # data = np.array(["My name is zhaokun","she is my wife i"])

    # 对中文进行分词,中文之间也必须用,不会统计单个汉字
    data = np.array(["我的 名字 叫 赵坤","她是我媳妇"])
    d = cv.fit_transform(data)

    print("type",type(d))

    # 获取特征值,特征值为单个单词,单词与单词之间使用空格来区分
    print(cv.get_feature_names())

    # 使用toarray()函数来转换为list类型数据,将sparse矩阵转换为array数组
    print(d.toarray())

# 示例5:对中文进行分词
'''
jieba中文分词

下载:在Anaconda prompt环境中pip install jieba
使用:import jieba
'''
def cutWord():

    data = "今天是个好天气,我们一家出去游玩,今天"

    # data = "今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。"
    d = jieba.cut(data)

    # 将数据转换为list数据,将其转换为多条样本数据,中间用,号隔开
    data = list(d)
    print(list(data))

    # 将list数据转换为字符串,之间用空格隔开
    data = ' '.join(data)

    print(data)

    cv = CountVectorizer()

    # 再将字符串数据转换为list数据,用[]括起来
    d = cv.fit_transform([data])

    print("type", type(d))

    print(cv.get_feature_names())

    print(d.toarray())

# 示例6:对多条中文进行分词
def cutWord1():

    data1 = "今天去打篮球"
    data2 = "明天去踢足球"

    c1 = jieba.cut(data1)
    c2 = jieba.cut(data2)

    c1 = list(c1)
    c2 = list(c2)

    print(c1)
    print(c2)

    # 用空格将list数据转换为字符串数据
    c1 = " ".join(c1)
    c2 = " ".join(c2)

    # 返回多个字符串的形式
    return c1,c2

def cutWord2(c1,c2):

    cv = CountVectorizer()

    # 再将字符串数据转换为list数据,用[]括起来,两条数据中间用,隔开
    d = cv.fit_transform([c1,c2])

    print("type:",type(d))
    print(cv.get_feature_names())

    print(d.toarray())

    print("type:",type(d.toarray))

# 示例7:tfidf
'''
TfidfVectorizer相当于CountVectorizer与TfidfTransformer二者的结合体

TF-IDF的主要思想是:如果某个词或短语在一篇文章中出现的概率高,并且在其他文章中很少出现,
则认为该词或短语具有很好的类别区分能力,适合用来分类
TF-IDF作用:用以评估字词对于一个文件集或者语料库中的其中一份文件的重要程度
'''
def tfidf1(c1,c2):

    tfidf = TfidfVectorizer()

    data = tfidf.fit_transform([c1,c2])

    print(tfidf.get_feature_names())

    print(data.toarray())

    print(tfidf.inverse_transform(data))

def tfidf2():
    # 语料
    corpus = [
        'This is the first document.',
        'This is the second second document.',
        'And the third one.',
        'Is this the first document?',
    ]
    # 将文本中的词语转换为词频矩阵
    vectorizer = CountVectorizer()
    # 计算个词语出现的次数
    X = vectorizer.fit_transform(corpus)
    # 获取词袋中所有文本关键词
    word = vectorizer.get_feature_names()
    print(word)
    # 查看词频结果
    print(X.toarray())

    # 类调用
    transformer = TfidfTransformer()
    print(transformer)
    # 将词频矩阵X统计成TF-IDF值
    tfidf = transformer.fit_transform(X)
    # 查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
    print(tfidf.toarray())

# 计算平均值与方差在线性回归的4文件中

# 特征抽取-->特征处理-->特征选择

if __name__ == "__main__":

    # dicFunction()
    fitFunction()
    # oneHot()
    # countVecor()
    # cutWord()

    # c1,c2 = cutWord1()
    # cutWord2(c1,c2)
    #
    c1, c2 = cutWord1()
    tfidf1(c1,c2)

    # tfidf2()