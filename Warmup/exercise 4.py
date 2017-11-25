#Exercise 4: A very big sum

import sys

def aVeryBigSum(n, ar):
    return sum(ar) #return the sum among the elements of the array

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)