#Exercise 7: Staircase
import sys


n = int(input().strip())
for i in range(1,1+n):  #for each line
    print(" "*(n-i) + "#"*i) #print space (repeated n-i times) concatenated to # (repeated i-times)