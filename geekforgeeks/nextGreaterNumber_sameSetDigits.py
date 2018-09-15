def swap(digitList, a, b):
    temp = digitList[a]
    digitList[a] = digitList[b]
    digitList[b] = temp
    

def nextGreaterNumber(digitList):
    #print digitList
    length = len(digitList)
    
    flag = False
    pos = 0
    for i in range(length-1, 0, -1):
        if digitList[i] > digitList[i-1]:
            pos = i-1
            flag = True
            break
    if flag is False:
        print("not possible")
    else:
        if pos == (length-1)-1:
            swappos = pos+1
            swap(digitList, pos, swappos)
        else:
            minimum = 10
            for i in range(pos+1, length, 1):
                if digitList[i] > digitList[pos]:
                    if digitList[i] - digitList[pos] < minimum:
                        minimum = digitList[i] - digitList[pos]
                        swappos = i
            
            swap(digitList, pos, swappos)
            
            digitList[pos+1:] = sorted(digitList[pos+1:])
        print(''.join(list(map(str, digitList))))

t = int(input())
for tc in range(t):
    n = list(input().strip())
    nextGreaterNumber(list(map(int, n)))