def removeEvens(k):

    newList = k
    numpopped = 0
    for i in range(0,len(k)):
        if newList[i - numpopped] % 2 == 0 and newList[i - numpopped] != 0:
            newList.pop(i - numpopped)
            numpopped = numpopped + 1
    
    return newList


print(removeEvens([1,2,3,4,5,6,7,8]))


