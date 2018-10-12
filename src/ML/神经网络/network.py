# https://blog.csdn.net/Mrzhang0419/article/details/79519994
from sklearn.neural_network import MLPClassifier
import numpy as np

X = [[0., 0.], [1., 1.]]
y = [0, 1]

clf = MLPClassifier(solver='sgd', alpha=1e-5, activation='logistic',
                    hidden_layer_sizes=(5, 2), max_iter=2000, tol=1e-4)
clf.fit(X, y)

predicted_value = clf.predict([[2., 2.], [-1., -2.]])
print(predicted_value)
predicted_proba = clf.predict_proba([[2., 2.], [-1., -2.]])
print(predicted_proba)

print([coef.shape for coef in clf.coefs_])
print([coef for coef in clf.coefs_])

# X = 2 * np.random.rand(100, 1)
#
# bias = np.random.randn(100, 1)
#
# Y = 4 + 3 * X + bias
#
# clf = MLPClassifier(solver='sgd', alpha=1e-5, activation='logistic',
#                     hidden_layer_sizes=(2, 1), max_iter=2000, tol=1e-4)
# clf.fit(X, Y)

# x = [[0.]]
#
# print(clf.predict(x))