from math import floor
#heapify
def maxHeapify(pos, arr):
    #print(pos)
    l = 2*pos+1
    r = 2*pos+2
    largest = pos
    if l < len(arr) and arr[l] > arr[largest]:
        largest = l
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    #swap arr[pos] and arr[largest]
    if largest is not pos:
        #print('swap {} {}'.format(pos, largest))
        temp = arr[pos]
        arr[pos]=arr[largest]
        arr[largest]=temp
        maxHeapify(largest, arr)
    return



def buildMaxHeap(arr):
    notleaf = floor(len(arr)/2 - 1)
    #print(notleaf)
    while notleaf >= 0:
        maxHeapify(notleaf, arr)
        notleaf = notleaf-1
    print(arr)


def extractMax(arr):
    #swap root with last element
    length = len(arr)-1
    temp = arr[length]
    arr[length]=arr[0]
    arr[0]=temp
    
    #pop last element
    print("{} is extracted".format(arr.pop()))
    
    maxHeapify(0, arr)
    print(arr)
    return

def increaseKey(arr, pos, value):
    arr[pos]+= value
    while pos > 0 and arr[pos] > arr[(pos-1)//2]:
        temp = arr[pos]
        arr[pos]=arr[(pos-1)//2]
        arr[(pos-1)//2]=temp
        pos = (pos-1)//2
    print(arr)
    return

def insertHeap(arr, value):
    arr.append(value)
    pos = len(arr)-1
    while pos > 0 and arr[pos] > arr[(pos-1)//2]:
        temp = arr[pos]
        arr[pos]=arr[(pos-1)//2]
        arr[(pos-1)//2]=temp
        pos = (pos-1)//2
    print(arr)
    return

if __name__=="__main__":
    
    arr = [1, 5, 6, 8, 12, 14, 16]
    buildMaxHeap(arr)

    extractMax(arr)

    increaseKey(arr, 6, 9)

    insertHeap(arr, 13)