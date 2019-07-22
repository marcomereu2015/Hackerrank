#Day 5
# Poisson Ditribution ~ Python 2

#input
avgX, avgY = [float(num) for num in raw_input().split(" ")]

# Cost
print(round(160 + 40*(avgX + avgX**2), 3))
print(round(128 + 40*(avgY + avgY**2), 3))

