import numpy as np

data = [1,2]

print("type:",type(data))

# list没有dtype属性
# print("dtype:",data.dtype)

data = np.array(data,dtype=np.str_)

# type获取数据类型
print("type:",type(data))

# dtype获取数据元素类型
print("dtype:",data.dtype)

# astype转换数据类型
data = data.astype(np.int)

# dtype获取数据元素类型
print("dtype:",data.dtype)

print(data.tostring())

print(data.tolist())

