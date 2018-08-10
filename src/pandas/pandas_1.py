import  pandas as  pd

# 示例1:读取excel表格

"""
info = pd.read_csv("food_info.csv")

# pandas中最重要的数据类型是DataFrame数据类型
print("数据类型")
print(type(info))

# print(info)

# 查看数据类型
print(info.dtypes)
"""

# 示例2: pandas中的head函数

"""
info = pd.read_csv("food_info.csv")

print(info.shape)

# 读取前面的数据,默认为开头5行数据
# print(info.head())

# 读取最开始的一行数据
print(info.head(1))
"""

# 示例3:获取指定位置的信息
"""
info = pd.read_csv("food_info.csv")

# 获取第0行的数据,不包括excel中头行数据
print(info.loc[0])

# 获取从第0行到第2行的数据
print(info.loc[0:2])

# 获取每字段名
print(info.columns)
"""


# 示例4: 获取指定行的指定列信息

"""
info = pd.read_csv("food_info.csv")

a = info.loc[0]

print(a)
# 一列信息直接填写
print(a["NDB_No"])

# 多列信息先定义矩阵
index = ["NDB_No","Shrt_Desc"]
print(a[index])
"""

# 示例5: 获取指定的多行数据

"""
info = pd.read_csv("food_info.csv")

# 先定义一个矩阵
rows = [1,2,5]

print(info.loc[rows])
"""

# 示例6:将属性转换为列表类型

info = pd.read_csv("food_info.csv")

attr = info.columns

print(type(attr))

# 转化为list类型
attr = attr.tolist()

print(type(attr))