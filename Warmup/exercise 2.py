#Exercise 2: Simple Array Sum
import sys

def simpleArraySum(n, ar):
    return sum(ar) #sum all the element in ar

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)