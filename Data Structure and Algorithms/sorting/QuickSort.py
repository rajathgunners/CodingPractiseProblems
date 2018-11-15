#  QuickSort

def partition(l, low, high):
    
    par = l[high]
    i = low-1
    
    for j in range(low, high):
        if l[j] <= par:
            i = i+1
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
    
    temp2 = l[i+1]
    l[i+1] = l[high]
    l[high] = temp2
    return i+1

def quickSort(l, low, high):
    
    if low < high:
        p = partition(l, low, high)
    
        quickSort(l, low, p-1)
        quickSort(l, p+1, high)






l = [10, 80, 30, 90, 40, 50, 70]
quickSort(l, 0, 6)
print(l)