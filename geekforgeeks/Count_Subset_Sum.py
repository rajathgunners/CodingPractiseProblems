# to count number of subsets with given (sum)  in list
l = [1, 3, 2, 5, 3, 4]

#print(l[1:])

def SubsetSum(l, sum):
    if sum is 0:
        return 1
    elif sum < 0 or not l:
        return 0
    else:
        return SubsetSum(l[1:], sum-l[0]) + SubsetSum(l[1:], sum)

print(SubsetSum(l,7))