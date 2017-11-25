#Exercise 14: The letter-lover Mystery
import sys

def theLoveLetterMystery(s):
    op=0 #number of operations
    for i in range(len(s)//2): #analize the 2 opposite elements in the string
        op += abs(ord(s[i]) - ord(s[-(i+1)])) #compute the number of reductions(==distance in the alphabet for each couple)
    return op


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)