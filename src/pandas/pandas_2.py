import  pandas as  pd

# https://blog.csdn.net/u011462357/article/details/78377411

#  读取excel表格
data = pd.read_excel('./data/1.xlsx')

# 读取csv文件,数据之间要用,隔开
# pd.read_csv('./data/1.xlsx',sep=',')
print(data)

# 按照特征Brand进行排序,并统计数量
'''
从结果中可以看到Brand分组后的这个结果,Name,Cloth,Count列在每种Brand所对应的行的数字都是一样的.
比如2 2 2可以理解为每种Brand各有多少行数据
'''
gp = data.groupby('Brand').count()

print(gp)

print('*********************')

# 统计次数大于>1
print(gp[gp.Name > 1])

#
tf = gp[gp.Name > 1].reset_index()

print(tf)

print('--------------------------')

# 获取过滤后的数据
data = data[data['Brand'].isin(tf.Brand)]

print(data)