#Exercise 12: Find the Median

def median(l,ar):
    ar=sorted(ar)  #sort the array

    # if the lenght is odd, return the middle element of the list
    if l%2!=0:
        return ar[l//2]
    # otherwise return the average between the two middle elements
    else:
        return (ar[l//2]+ ar[(l//2)-1])/2



n= int(input().strip())
arr=[int(x) for x in input().split()]
print(median(n,arr))
