# Quick Sort: 

def swap(lst, index1, index2):
    temp=lst[index1]
    lst[index1]=lst[index2]
    lst[index2]=temp

def pivot(lst, pivot_index, ending):
    swap_index=pivot_index
    for x in range(pivot_index+1, ending+1):
        if lst[x]<lst[pivot_index]:
            swap_index+=1
            swap(lst, swap_index,x)
    swap(lst, pivot_index, swap_index)
    return swap_index

def quicksort_helper(lst, left, right):
    if left< right:
        pivot_index= pivot(lst, left, right)
        quicksort_helper(lst, left, pivot_index-1)
        quicksort_helper(lst, pivot_index+1, right)
    return lst

def quicksort(lst):
    return quicksort_helper(lst, 0, len(lst)-1)


print(quicksort([5,34,36,6,6,4634,665,36,6,33]))
