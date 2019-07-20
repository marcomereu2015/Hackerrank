#hackerranck Statistics Day 1
#Standard Deviation

from math import sqrt
N = input()
X = map(float,raw_input().split())
mean = sum(X)/N
print round(sqrt(sum([(x-mean)**2 for x in X])/N),1)
