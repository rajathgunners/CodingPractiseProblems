"""Find the minimum number of reversals so that maximum pair of strings are similar"""
def CountReversedStrings(arr):
    sdict = {}# store all the occurences of strings in arr
    rdict = {}# store all the strings which has been reversed in sdict 
    for i in arr:
        if i in sdict:
            sdict[i] += 1
        else:
            sdict[i] = 1
    
    count = 0
    for i in sdict:
        if i not in rdict:
            t = "".join(reversed(i))
            if t in sdict:
                if sdict[t] < sdict[i]:
                    count += sdict[t]
                else:
                    count += sdict[i]
                
                rdict[t] = True
    
    print(sdict)
    return count

arr = input().strip().split()
print(CountReversedStrings(arr))
    