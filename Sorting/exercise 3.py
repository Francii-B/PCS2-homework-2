#Exercise 3: Insertion sort Part 1

def sorting(l, el, arr):
    #as long as the current element (l) is smaller than the previous one (el), and the list is not ended...
    while (int(arr[l]) > int(el)) and (l>= 0):
            arr[l+1]= arr[l] # ...the current element is equal to the previous one
            print(' '.join(arr)) #print the list
            l-=1 #pass to the previous position in the list

    # once found the right position, insert the unsorted element
    arr[l+1]= el
    print(' '.join(arr)) #print the final list



l = int(input().strip()) - 2 #max number of comparisons (number of elements, excluding the last element)
ar=input().split() #take the elements
sorting(l,ar[-1], ar )
