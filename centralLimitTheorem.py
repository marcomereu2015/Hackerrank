#Day 6
#the Central Limit Theorem ~ Python 2


import math

mean = 205
sigma = 15
n = 49
x = 9800

def cdf(x, mean, std):
    return round(0.5 * (1 + math.erf((x - mean)/ (std * math.sqrt(2)))), 4)

print cdf(x, n * mean, math.sqrt(n) * sigma)