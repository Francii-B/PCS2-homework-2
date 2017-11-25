#Exercise 3: Compare the triplets

import sys


def solve(a0, a1, a2, b0, b1, b2):
    a,b= 0, 0 #create the scores
    for i, j in [[a0,b0],[a1,b1],[a2,b2]]: #compare each couples
        if i > j:
            a+=1
        elif i< j:
            b+=1
    return [a , b] #return the two scores

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))