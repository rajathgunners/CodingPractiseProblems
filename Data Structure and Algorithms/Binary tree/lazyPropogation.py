#Lazy Propogation - MAX or MIN after many queries of sum in range(x,y)
import sys
import math

def lazyProp(start, end, alow, ahigh, k, i):
    global st, lpt
    mid = (alow + ahigh)//2
    
    if lpt[i] is not 0:
        st[i] = st[i] + lpt[i]
        if alow is not ahigh:
            lpt[2*i+1] = lpt[i]
            lpt[2*i+2] = lpt[i]
        lpt[i] = 0
    
    #full overlap
    if alow >= start and ahigh<= end:
        st[i] = st[i] + k
        if alow is not ahigh:
            lpt[2*i+1] = lpt[2*i+1] + k
            lpt[2*i+2] = lpt[2*i+2] + k
        return st[i]
    
    #no full overlap
    else:
        
        #no overlap
        if ahigh < start or alow > end:
            return st[i]
            
        #partial overlap
        else:
            st[i] = max(lazyProp(start, end, alow, mid, k, 2*i+1), lazyProp(start, end, mid+1, ahigh, k, 2*i+2))
            return st[i]


st = [7, 4, 7, 2, 4, 7, 3, -1, 2, 4, 1, 7, 1, 3, 2]
lpt =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for a0 in range(5):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        maxval = lazyProp(a, b, 0, 7, k, 0)
print(maxval)