Day 1. Quartiles


num = int(raw_input())
numbers = sorted(map(int, raw_input().split()))
center = len(numbers) // 2 # floor division

def median(median_numbers):
    #return np.median(median_numbers) # will work if numpy import is allowed
    middle = len(median_numbers) // 2  # floor division
    if (len(median_numbers) % 2 == 0):  # even or odd
        return (median_numbers[middle-1] + median_numbers[middle]) / 2
    else:
        return median_numbers[middle]

    
# actual program starts here    
if (len(numbers) % 2 == 0):    # even or not
    L = median(numbers[:center])
    R = median(numbers[center:])
else:
    # if odd set of numbers
    L = median(numbers[:center])
    R = median(numbers[center+1:])

print L
print median(numbers)
print R
