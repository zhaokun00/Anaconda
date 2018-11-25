'''
深度学习:如深度神经网络、卷积神经网络和递归神经网络已被应用计算机视觉、语音识别、自然语言处理、音频识别与
生物信息学等领域并获取了极好的效果

深度学习框架:
    TensorFlow、Caffe、Torch、deeplearning4j、CNTK、DSSTNE

    TensorFlow:
        1.全面的深度学习框架
        2.支持非常全面
        3.不是专门为客户端设计

        1.Goole Brain计划产物
        2.应用于AlphaGo,Gmail,Goole Maps等1000多个产品

        特点:
            1.真正地可移植性
            引入各种计算设备的支持包括CPU/GPU/TPU以及能够很好地运行在移动端,如安卓设备、ios、树莓派等等

            2.多语言支持
            TensorFlow有一个合理的c++使用界面,也有一个易用的python使用界面来构建和执行你的graphs,也可以直接写python/c++程序

            3.高度的灵活性与效率
            TensorFlow是一个采用数据流图,用于数值计算的开源软件库能够灵活进行组装图,执行图

            4.支持
            TensorFlow由谷歌提供支持,谷歌投入了大量的精力开发TensorFlow,它希望Tensorflow能够成为机器学习
            研究人员的通用语言

            5.现在采用的TensFlow版本为1.11.0版本,原因在于在0.12版本后支持可视化

            6.在进行深度学习时,由于很多样本大多是图片或语音等,或导致数据量大,样本多,算法本身设计复杂,因此计算
            时间很长,可能需要几小时或者几天,同时需要等待很长时间去优化,因此就有了GPU

            CPU和GPU之间的区别:
            CPU:只要运行的是操作系统,处理业务逻辑,计算能力不是特别突出,类似于一个高中生,综合素质比较高
            GPU:专门为计算而设计的,计算能力特别突出,类似于1000个小学生,可以同时进行计算
在编译TensFlow程序时报错,原因在于之前做朴素贝叶斯实验时安装了旧版本的numpy和h5py
pip install numpy --upgrade
pip uninstall h5py
'''

# 示例1:一般python中函数的定义及调用
def add(a,b):
    return a+b


# 导入tensorflow的包
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def tfadd():
    a = tf.constant(10)
    b = tf.constant(20)

    sum = tf.add(a,b)

    with tf.Session() as sess:
        print(sess.run(sum))

def tfsub():
    a = tf.constant(10)
    b = tf.constant(20)

    sub = a - b

    with tf.Session() as sess:
        print(sess.run(sub))

if __name__ == "__main__":

    # sum = add(1, 2)
    # print(sum)

    # tfadd()

    tfsub()