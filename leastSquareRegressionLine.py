#Day 8
#Least Square Regression Line   ~ Python 3


X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

#assuming len(X) == len(Y)
#b = mean(Y)*a*mean(X)
b = (len(X)*sum([X[i]*Y[i] for i in range(len(X))]) - sum(X)*sum(Y)) / (len(X)*sum([X[i]**2 for i in range(len(X))]) - sum(X)**2)
a = sum(Y)/len(Y) - b*(sum(X)/len(X))

#statistics' score = mean(y) = b + a(80)
print(round(a+b*80, 3))