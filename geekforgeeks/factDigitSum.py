arr = [1,1,0,0,0,0,0,0,0,0]


def fact(n):
    global arr
    #print(n)
    if arr[n] != 0:
        return arr[n]
    else:
        arr[n] = n * fact(n-1)
        return arr[n]

fact(9)
print(arr)
    

finallist = []
def digitFactSum(arr, pos, sums, lists):
    if finallist:
        return True
    if pos < 0:
        return False
    newsums = sums - arr[pos]
    if newsums < 0:
        return digitFactSum(arr, pos-1, sums, lists)
    elif newsums == 0:
        lists.append(str(pos))
        finallist.append(lists)
        return True
    elif newsums >= arr[pos]:
        return digitFactSum(arr, pos, newsums, lists + [str(pos)]) or digitFactSum(arr, pos-1, sums, lists)
    else:
        return digitFactSum(arr, pos-1, newsums, lists + [str(pos)]) or digitFactSum(arr, pos-1, sums, lists)

if digitFactSum(arr, 9, 40321, []):
    ans = finallist[0]
    ans.reverse()
    ans = ''.join(ans)
    print(ans)

   
    

        
    