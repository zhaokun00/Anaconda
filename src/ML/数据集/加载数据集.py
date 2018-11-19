import sklearn.datasets as skdata

# https://www.cnblogs.com/nolonely/p/6980160.html
# data = skdata.load_iris()
#
# print("type:",type(data))
# print("data:",data.data)
# print("DESCR:",data.DESCR)
# print("target:",data.target)

data = skdata.fetch_20newsgroups()

print("type:",type(data))
print("data:",data.data)
print("DESCR:",data.DESCR)
print("target:",data.target)