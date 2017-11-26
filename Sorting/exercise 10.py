#Exercise 10: The Full Counting Sort

def CountingSort(n):
    dict={} #create a dictionary
    for x in range(n):
        pos, w= input().split() #each input is splitted in 2: position and string
        pos= int(pos) #convert the position into an integer

        # if the input belongs to the first half of inputs, replace the string with '-'
        if x < (n//2):
            w= '-'

        # if the key (position) is already in the dictionary, add the string to the values already present
        if pos in dict:
            dict[pos]+= [w]
        else: #otherwise create it
            dict[pos] = [w]

    # join all the values, according to their position(key)
    for pp in range(max(dict)+1):
        if pp in dict:
            print(' '.join(dict[pp]),end=' ')



ll=int(input().strip()) #number of inputs
CountingSort(ll)
