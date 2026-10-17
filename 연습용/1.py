from sklearn import svm
x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]

a = svm.SVC()
a.fit(x,y)
pre = a.predict([[0,0],[1,1]])
print(pre)