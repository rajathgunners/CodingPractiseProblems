# to find all subsets which add to a given SUM in a set, Repetition allowed

from copy import deepcopy
l = [3, 2, 5, 10, 6]
finallist = list()
#print(l[1:])

def SubsetSum(l, sums, sumlist):
    if sums is 0:
        finallist.append(sumlist)
        return 
    elif sums < 0 or not l:
        return
    elif sums - l[0] >= l[0]:
        SubsetSum(l, sums-l[0], sumlist + [l[0]])
        SubsetSum(l[1:], sums, sumlist)
        
    else:
        SubsetSum(l[1:], sums-l[0], sumlist + [l[0]])
        SubsetSum(l[1:], sums, sumlist)

SubsetSum(l, 10, [])
print(finallist)