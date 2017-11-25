#Exercise 9: Birthday Cake Candles
import sys


def birthdayCakeCandles(n, ar):
    return ar.count(max(ar)) #count the occurrences of the highest 'height'


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)