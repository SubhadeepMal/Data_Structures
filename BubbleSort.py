# Bubble Sort:

def bubblesort(lst):
    for x in range(len(lst)-1, 0, -1):
        for y in range(x):
            if lst[y]>lst[y+1]:
                temp=lst[y]
                lst[y]=lst[y+1]
                lst[y+1]=temp
    return lst


print(bubblesort([5,34,36,6,6,4634,665,36,6,33]))