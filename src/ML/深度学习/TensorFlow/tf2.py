import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 示例1:TensorFlow中的图
'''
在pycharm中
    f:表示属性
    m:表示方法
    c:表示类
    p:表示属性
    
图默认已经注册,一组表示tf.Operation计算单位的对象和tf.Tensor表示操作之间流动的数据单元的对象

Tensor:表示张量,即表示数据
Flow:表示操作
'''
def test1():

    # 获取默认的图
    graph = tf.get_default_graph()

    print("默认图:",graph)

    data = tf.constant(4)

    # 通过张量获取图
    print("张量的图:",data.graph)

    sess = tf.Session()

    # 通过session获取图
    print("sess的图:",sess.graph)

    g = tf.Graph()
    print("创建了一张图:",g)

    # 将创建的图作为当前的图
    with g.as_default():
        a = tf.constant(1)

        with tf.Session() as sess:
            print(sess.graph)
# 示例2:session的第一种使用方法
def test2():

    data1 = tf.constant(3)
    data2 = tf.constant(2)

    sum = data1 + data2;
    sess = tf.Session();

    # print(sess.run(sum))
    s = sess.run(sum)

    print("相加和:",s)
    print("类型:",type(s))

    sess.close()

# 示例3:session的第2种使用方法,相较于第一种用法更加简便,session不用再close掉
def test3():

    data1 = tf.constant(3)
    data2 = tf.constant(2)

    sum = data1 + data2;

    with tf.Session() as sess:
        print(sess.run(sum))

if __name__ == "__main__":

    test1()

    # test2()

    # test3()