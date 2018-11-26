import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# https://blog.csdn.net/czp11210/article/details/51161520
# https://blog.csdn.net/gaotihong/article/details/82111183?utm_source=blogxgwz4
def naviebayes():

    news = fetch_20newsgroups(subset='all')

    print(type(news))

    # 分类的名称
    print("target_name:",news['target_names'])
    # 文件名
    print("filenames:",news['filenames'])
    for it in news:
        print(it)

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

    # 对数据集进行特征抽取
    tf = TfidfVectorizer()

    # 以训练集当中的词的列表进行每篇文章重要性统计['a','b','c','d']
    x_train = tf.fit_transform(x_train)

    print(tf.get_feature_names())

    # 对测试数据进行数据转换
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

if __name__ == "__main__":

    naviebayes()