#Exercise 6: Plus Minus
import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

p=sum([1 for i in arr if i > 0]) #count the positive elements
neg=sum([1 for i in arr if i < 0]) #count the negative
print(format(p/n,".6f")) #print the positive fraction ( .6 is the precision)
print(format(neg/n,".6f")) #print negative fraction
print(format(abs(n-p-neg)/n, ".6f")) #print zeroes