#Exercise 5: Mars Exploration
import sys


S = input().strip()
diff=[1 for i in range(len(S)) if 'SOS'[i%3] != S[i]]  #compare each letter of the two strings, and note the differences
print(sum(diff)) #print the number of mistakes