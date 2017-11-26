#Exercise 4: Insertion sort Part 2


def insertionSort(arr,lenght):
    for i in range(1,lenght): #find the position on each element by calling the function FindPos
        arr=FindPos(i, arr)
        print(' '.join(arr)) #print each new sorted list


def FindPos(l, arr):
    for j in range(l): #compare the element l with the previous ones (already sorted)
        if int(arr[j]) > int(arr[l]) : #if the l-element is smaller than the current one, swap the positions
            arr.insert(j, arr.pop(l))
            return arr
    return arr


lenght=int(input().strip())
a=input().split()
insertionSort(a, lenght)

