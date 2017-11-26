#Exercise 6: Running Time of Algorithms

def insertionSort(arr,lenght):
    sh=0 #number of shifts
    for i in range(1,lenght): #for each element find its position by calling the function FindPos
        s, arr= FindPos(i, arr)
        sh+= s
    print(sh) #print the total number of shifts

def FindPos(l, arr):
    for j in range(l): #for each element before arr[l], find the first one which is higher than it
        if int(arr[j]) > int(arr[l]) :
            arr.insert(j, arr.pop(l)) #swap the positions
            return [ l-j, arr ] #return the shifts and the new sorted list
    return [ 0, arr ] #return 0 shifts if the element arr[l] is the highest one


lenght=int(input().strip())
a=input().split()
insertionSort(a, lenght)