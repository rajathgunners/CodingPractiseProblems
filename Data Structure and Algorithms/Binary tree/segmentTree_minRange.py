#SEGMENT TREE(minimum in a range(x,y) of given array 'arr')
import numpy, math

#creating segment tree using array
def segmentTree(arr, start, end, i):
    global st
   
    if start < end:
        mid = (start + end)//2
        segmentTree(arr, start, mid, 2*i+1)
        segmentTree(arr, mid+1, end, 2*i+2)
    
    else:
        st[i] = arr[start]
        return
    
    st[i] = min(st[2*i+1], st[2*i+2])
    return

#Finding min in a range using segmentTree
def ST_findMin(st, start, end, alow, ahigh, i):
    #full overlap
    if (alow >= start and alow <= end) and (ahigh >= start and ahigh <= end):
        return st[i]
    
    #no full overlap
    else:
        #no overlap
        if (alow < start and ahigh < start) or (alow > end and ahigh > end):
            return 1000
        #partial overlap
        else:
            return min(ST_findMin(st, start, end, alow, (alow+ahigh)//2, (2*i+1)), ST_findMin(st, start, end, ((alow+ahigh)//2)+1 , ahigh, (2*i+2)))
        
            
        
    
   
        


arr = [-1, 3, 4, 0, 2, 1]
st = numpy.empty(int(2 * math.pow(2, math.ceil(math.log2(len(arr))))-1), dtype=object)
segmentTree(arr, 0, len(arr)-1, 0)
print(arr)
print()
print(st)
print()
print(ST_findMin(st, 1, 1, 0, 5, 0))