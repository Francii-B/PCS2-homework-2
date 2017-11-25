#Exercise 17:Anagram
import sys

def anagram(s):
    if len(s) % 2 != 0: #if the lenght is odd, the anagram cannot be found
        return -1

    l=len(s)// 2 #find the middle point of the list
    changes={}

    for i in s[:l]:  #find the occurrences of each character in the first half of the list
        if i in changes:
            changes[i] += 1
        else:
            changes[i] = 1

    for el in s[l:]: #compare with the second half of the list, to find the differences
        if (el in changes) and (changes[el]>0) :
            changes[el]-=1

    return sum(changes.values()) #the remaining values correspond to the differences
    

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
