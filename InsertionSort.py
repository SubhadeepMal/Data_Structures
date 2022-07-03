# Insertion Sort:

def insertionsort(lst):
    for x in range(len(lst)-1):
        for y in range(x+1,0,-1):
            if lst[y]<lst[y-1]:
                temp=lst[y]
                lst[y]=lst[y-1]
                lst[y-1]=temp
    return lst

print(insertionsort([99,34,12,203,0,2,45]))