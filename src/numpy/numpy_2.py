import numpy as np

# 示例1:ndarray类型变量比较

"""
list1 = [1,2,3]

array1 = np.array(list1)
# 输出也是一个ndarray类型的变量,存储的是各个数据比较的结果,直接用变量与被比较的变量相互比较

# 一维矩阵的比较
var = (array1 == 2)
print(array1)
print(var)

print(array1[var])
list2 = [4,5,2]
array2 = np.array([list1,list2])
# 二维矩阵的比较,输出结果也是二维矩阵
var = (array2 == 1)
print(array2)
print(var)
print(array2[var])

# 从矩阵中获取=1和=2的数据
var = (array2 == 1) | (array2 == 2)
print(var)
print(array2[var])

# 获取指定的值,并且给指定的值赋值
var = (array2 == 1) | (array2 == 2)
array2[var] = 10
print(array2)
"""

# 示例2:进行数据类型转换

"""
list1 = [1,2,3]

array1 = np.array(list1)

print(array1)

# 强制转化为str类型
array1= array1.astype(np.str)

print(array1)

"""

# 示例3:计算求和

"""
list1 = [1,2,3]
list2 = [1,2,3]

array1 = np.array(list1)
array2 = np.array([list1,list2])
# 对行矩阵进行求和
vector1 = np.sum(array1,0)

# 对每一列数据进行相加求和
vector2 = np.sum(array2,0)

# 对每一行数据相加求和
vector3 = np.sum(array2,1)

print(vector1)

print(vector2)

print(vector3)

"""

# 示例3:计算平均值

"""
list1 = [1,2,3]
list2 = [1,2,3]

array2 = np.array([list1,list2])

# 对每一列数据进行相加求和
vector2 = np.sum(array2,0)

print(vector2)

# 最终计算出一个值
vector2 = np.mean(vector2)

print(vector2)

"""

# 示例4:读取文本,筛选为空的的数据,并赋值为字符0

info = np.genfromtxt("world_alcohol.txt",delimiter=",",skip_header=1)

# print(info[0,:])
# print(np.isnan(info[0,4]))
#
# print(info[24,:])
# print(np.isnan(info[24,4]))

# 查看哪一行数据里面没有数据
var = np.isnan(info[:,4])

print(var)

# 获取为空的那一行数据
vector1 = info[var,:]

print(vector1)

# 给空的那一行数据赋值为字符0
info[var,4] = "0"

vector1 = info[var,:]

print(vector1)

"""
matrix = np.array([
                [5, 25, 15],
                [20, 25, 30],
                [35, 40, 45]
             ])

# 判断第一列数据是否等于25
second_column_25 = (matrix[:,1] == 25)

print(second_column_25)

# 打印第0行与第1行数据
print(matrix[second_column_25, :])
"""