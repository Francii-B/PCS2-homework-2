#Exercise 8: Counting Sort 1


def counting(n,ar):
    ord=[0]*100  #create an list in which each position corresponds to a number of the array 'arr'
    for x in ar: #count the occurrences of each element
        ord[int(x)] += 1

    print(' '.join(map(str, ord))) #print all the occurrences


n=int(input().strip())
ar= input().split()

counting(n,ar)
