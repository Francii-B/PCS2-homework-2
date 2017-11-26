#Exercise 9: Counting Sort 2
input()
ar=input().split()

def sorting(ar):
    ord=[0]*100  #create a new list as counter
    for x in ar: #count all the occurrences
       ord[int(x)] += 1

    for pos in range(100): #print all the sorted elements, according to their occurrence
       print(ord[pos]*(str(pos) +' '), end='')