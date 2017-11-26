#Exercise 7: Quicksort 1 - Partition

def Quicksort(arr):

    # if the list is longer than 1...
    if len(arr) > 1:
        piv=arr[0] # fix the pivot
        R, L = [], []  # right and left list
        # compare each element (excluding the pivot) of the list with the pivot
        for i in range(1,len(arr)):
            if int(piv) > int(arr[i]):
                L.append(arr[i])
            else:
                R.append(arr[i])
        # concatenate the 3 list, in which L and R are sorted by recursion of the function
        return Quicksort(L) + [piv] + Quicksort(R)

    # otherwise, if the list is composed by 0 or 1 element, return the list itself
    else:
        return arr

input()
ar= input().split()
print(' '.join(Quicksort(ar)))