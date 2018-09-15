# to check if subset with given sum exists in list
l = [1, 3, 2, 5]

#print(l[1:])

def SubsetSum(l, sum):
    if sum is 0:
        return True
    elif sum < 0 or not l:
        return False
    else:
        return SubsetSum(l[1:], sum-l[0]) or SubsetSum(l[1:], sum)

if SubsetSum(l, 6):
    print("exists")
else:
    print("not exists")