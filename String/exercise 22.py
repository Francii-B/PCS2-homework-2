#Exercise 22: Sherlock and the valid string
import sys

def isValid(s):
    an={} #dict in which the keys are the frequencies of each character and the values are the frequencies of the keys
    for i in set(s):  #for each different character, count its frequency
        rep=s.count(i)
        if rep in an: #add it to the dictionary
            an[rep] += 1
        else:
            an[rep] = 1
    #if all the characters occur the same number of times, it's 'Valid'
    if len(an)==1:
        return 'YES'
    #if there are two kind frequencies, we must check if...
    elif len(an)==2:
        m=min(an.keys())
        M=max(an.keys())
        #...the difference among the two keys is 1 and if one of the occurs only one time
        if (1 in an.values()) and ((M-m)==1):
            return 'YES'
        #...or if the different key, that is equal to 1, occurs only once
        elif (1 in an.keys()) and (an[1]==1):
            return 'YES'
        #otherwise it's 'Not Valid'
        else:
            return 'NO'
    #if the frequencies are more than two, it's 'Not Valid'
    else:
        return 'NO'

s = input().strip()
result = isValid(s)
print(result)
