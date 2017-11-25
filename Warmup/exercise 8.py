#Exercise 8: Mini-Max Sum
import sys

arr = list(map(int, input().strip().split(' ')))
print(sum(arr)-max(arr), sum(arr)-min(arr)) #print the minimum sum (sum of elements - max value) and maximum sum