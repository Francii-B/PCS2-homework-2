#Exercise 1: Big Sorting
import sys

n = int(input().strip())
unsorted = []
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)

print('\n'.join(sorted(unsorted, key=int))) #print the sorted elements, by int-increasing-order

