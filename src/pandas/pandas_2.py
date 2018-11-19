import  pandas as  pd

# https://blog.csdn.net/u011462357/article/details/78377411
# 示例1:读取excel表格
data=pd.read_excel('./data/1.xlsx')

print(data)

print('-------------------------')

gp=data.groupby('Brand').count()

print(gp)

print('*********************')

print(gp[gp.Name > 1])

tf = gp[gp.Name > 1].reset_index()

print(tf)

print('--------------------------')

data = data[data['Brand'].isin(tf.Brand)]

print(data)