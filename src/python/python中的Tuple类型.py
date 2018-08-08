"""
元组(tuple)与列表类似,不同之处在于元组的元素不能修改,元组写在小括号()里,元素之间用逗号隔开
元素中的元素类型也可以不相同
"""

# 定义元组
tuple1 = (1,2,3)
print("tuple1:",tuple1)

# 元组不能进行修改
# tuple1[0] = "zhaokun"
# print("tuple1:",tuple1)

#
# tuple1[3] = "zhaokun"
# print("tuple1:",tuple1)

# 元组进行连接
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print("tuple3:",tuple3)

# 元组可以重新进行赋值
tuple1 = (5,2,3)
print("tuple1:",tuple1)