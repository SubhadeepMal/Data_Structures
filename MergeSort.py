# Merge sort:

def merge(arr1, arr2):
    final=[]
    i=j=0

    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            final.append(arr1[i])
            i+=1
        else:
            final.append(arr2[j])
            j+=1

    while i<len(arr1):
        final.append(arr1[i])
        i+=1

    while j<len(arr2):
        final.append(arr2[j])
        j+=1

    return final

def mergesort(lst):
    if len(lst)==1:
        return lst
    mid=int(len(lst)/2)
    left=lst[:mid]
    right=lst[mid:]
    return merge(mergesort(left), mergesort(right))

print(mergesort([5,34,36,6,6,4634,665,36,6,33]))