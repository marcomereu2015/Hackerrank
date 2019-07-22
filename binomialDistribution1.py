#Day 4
#binomial Distribution 2


from math import factorial

#bd ... Binomial Distribution
def bd(n, r, p): 
    #q = 1 - p
    return (factorial(n)/(factorial(r)*factorial(n-r))) * p**r * (1 - p)**(n-r)

print (round (sum( [bd(10, i, .88) for i in range (8, 11)]), 3))
print (round (sum( [bd(10, i, .12) for i in range (2, 11)]), 3))