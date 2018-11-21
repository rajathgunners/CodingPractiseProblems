"""Find the count of good pairs i.e sum of indexes(i, j) == sum of values(arr[i], arr[j]) whre i<j"""
def GoodPairs(arr):
    sdict = {}
    for pos, i in enumerate(arr):
        t = pos-i
        if t in sdict:
            sdict[t] += 1
        else:
            sdict[t] = 1
    
    count = 0
    for pos, i in enumerate(arr):
        t = -1*(pos-i)
        if t in sdict:
            count += sdict[t]
        sdict[-1*t] -= 1
    
    return count

arr = list(map(int, input().strip().split()))
print(GoodPairs(arr))