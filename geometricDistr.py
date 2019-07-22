#Day4
# Geometric Distribution ~ Python3



def geoD(n, p):
    return (1-p)**(n-1) * p
   
print(round(sum([geoD(i, 1/3) for i in range(1,6)]), 3))