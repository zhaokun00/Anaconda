import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from numpy import float64

# https://www.cnblogs.com/erbaodabao0611/p/7588840.html
x_train = [[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]]

y_train = [0,0,0,1,1,1]

# print(x_train)
# print(y_train)

# https://segmentfault.com/q/1010000005183261/a-1020000005336946
x_train = np.array(x_train,dtype=float64)
y_train = np.array(y_train)

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)

print(x_train)
print(y_train)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(x_train,y_train)

x_test = [[4,100]]

x_test = scaler.transform(x_test)
y_test = [0]

result = knn.predict(x_test)

score = knn.score(x_test,y_test)

print(result)
print(score)
