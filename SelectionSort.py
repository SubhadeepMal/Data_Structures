# Selection Sort:

def selectionsort(lst):
    for x in range(0,len(lst)-1):
        minindex=x
        for y in range(x+1, len(lst)):
            if lst[minindex]>lst[y]:
                minindex=y
        temp=lst[x]
        lst[x]=lst[minindex]
        lst[minindex]=temp
        print(lst)
    return lst

print(selectionsort([5,34,36,6,6,4634,665,36,6,33]))