def myBisectLeft(arr, x, lo=0, hi=-1, K=1):
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
