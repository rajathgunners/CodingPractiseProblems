#Finds the position in the sorted array to insert the new element such that the array remains sorted
# bisect_left -> arr[0:lo] < x(insertion element) ; arr[lo:hi] >= x
#bisect_right -> arr[0:lo] <= x(insertion element) ; arr[lo:hi] > x

def myBisectRight(arr, x, lo=0, hi=-1):
    if hi == -1:
        hi = len(arr)
    
    if lo==hi:
        return lo
    
    while lo < hi:
        mid = (lo+hi)//2
        
        if arr[mid] > x:
            hi = mid
        
        elif arr[mid] <= x:
            lo = mid+1
    
    return lo

def myBisectLeft(arr, x, lo=0, hi=-1):
    if hi == -1:
        hi = len(arr)
    
    if lo==hi:
        return lo
    
    while lo < hi:
        mid = (lo+hi)//2
        
        if arr[mid] >= x:
            hi = mid
        
        elif arr[mid] < x:
            lo = mid+1
    
    return lo

if __name__ == "__main__":
    pass
