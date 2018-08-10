# numpy是一个python包,它是一个由多维数组对象和用于处理数组的例程集合组成的库,可以认为是一个处理矩阵的库
import numpy as np

# 示例1:从txt文本中读取数据
"""
# fname:文件名
# dtype:数据类型
# delimiter:字段的分隔符
# skip_header:跳过头几行数据
"""
"""
info = np.genfromtxt("world_alcohol.txt",dtype=np.str,delimiter=",",skip_header=1)

# 对于numpy中最重要的数据类型是ndarray类型
print("数据类型")
print("type:",type(info))

print("形状")
print("shape:",np.shape(info))

print(info)
"""

# 示例2:将python中列表类型转换为ndarray数据类型
"""
# 定义了python中的列表
list1 = [1,2,3]
array1 = np.array(list1)

print("数据类型")
print("type:",type(array1))

print("形状")
# 转换为一维矩阵,一维矩阵shape打印的是矩阵中元素的个数
print("shape:",np.shape(array1))

print("数据")
print(array1)

list2 = [5,6,7]

# 用2个列表类型,拼接成一个2维数组,列表用中括号[]括起来,组成二维矩阵时列表必须元素的个数是相等的
array2 = np.array([list1,list2])

print("数据类型")
print("type:",type(array2))

print("形状")
# 转换为二维矩阵,shape函数显示的行数与列数
print("shape:",np.shape(array2))

print("数据")
print(array2)
"""

# 示例3:打印ndarray类型的变量中的数据类型
"""
list1 = [1,2,3]
list2 = ["1","2","3"]
list3 = [1.0,2.0,3.0]

array1 = np.array(list1)
array2 = np.array(list2)
array3 = np.array(list3)

# int32类型
print(array1.dtype)
# 字符串类型
print(array2.dtype)
# float64类型
print(array3.dtype)
"""

# 示例4:访问ndarray类型变量中的数据
"""
info = np.genfromtxt("world_alcohol.txt",dtype=np.str,delimiter=",",skip_header=1)

# 访问0行0列数据
print(info[0,0])

# 访问第0行的数据,所有列
print(info[0])

# 访问第0列的数据,所有行
print(info[:,0])

# 访问从第0行到第2行，第0列到第2列的数据
print(info[0:2,0:2])
"""