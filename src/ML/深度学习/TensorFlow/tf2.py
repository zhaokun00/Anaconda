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

# eval函数,相当于进行run函数
def test4():

    data1 = tf.constant(3)
    data2 = tf.constant(2)

    sum = data1 + data2;

    with tf.Session() as sess:
       #  eval函数,获取返回值,相当于进行run函数
       print(sum.eval())

# config=tf.ConfigProto(log_device_placement=True),可以打印当前程序在哪个CPU上运行
def test5():

    data1 = tf.constant(3)
    data2 = tf.constant(2)

    sum = data1 + data2;

    with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
        sess.run(sum)

# placeholder函数:占位符,在程序执行的时候,不确定输入的是什么,run函数运行时通过feed_dict指定参数,一般是用于训练时输入数据使用
def test6():

    data1 = tf.placeholder(tf.float64)
    data2 = tf.placeholder(tf.float64)

    sum = data1 + data2

    with tf.Session() as sess:
        # 错误的写法
        # print(sess.run(sum,feed_dict={"data1":1,"data2":3}))
        # 正确的写法,feed_dict实际是一个map类型
        print(sess.run(sum, feed_dict={data1: 1, data2: 3}))

#  placeholder函数,指定形状
def test7():

    # 第二个参数规定了占位符的形状
    data1 = tf.placeholder(tf.float64,[2,3])
    # 当函数并不确定时可以用None进行表示,因此在用使用feed_dice表示时可以输入任意的行数
    # data1 = tf.placeholder(tf.float64,[None,3])
    # data1为一个tensor
    print(data1)

    print(type(data1))
    with tf.Session() as sess:
        print("***************")
        print(sess.run(data1, feed_dict={data1: [[1,2,3],[4,5,6]]}))
        print("***************")
        print(data1.shape)
        print("***************")
        print(data1.name)
        print("***************")
        print(data1.op)

if __name__ == "__main__":

    # test1()

    # test2()

    # test3()

    # test4()

    # test5()

    # test6()

    test7()