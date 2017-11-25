#Exercise 10: Funny String

import sys

def funnyString(s):
    for i in range(1,len(s)//2): #compare the two halves of the list
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(s[-i])-ord(s[-i-1])): #if s[i+1]-s[i] is different from s[-1-i]-[-2-i]...
            return 'Not Funny' #return not Funny

    return 'Funny' #otherwise Funny

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)