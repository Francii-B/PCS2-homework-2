#Exercise 5: Diagonal Difference
import sys


n = int(input().strip()) #dimentions of the matrix
dif=0 #initial difference between diagonals
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')] #each row is recorded as an array of integers
    dif+= a_t[a_i]- a_t[-1-a_i] #in each row, compute the difference among the two elements of the diagonals, and add it to the previous difference
print(abs(dif)) #print the absolute difference