"""Given a string s, recursively remove adjacent duplicate characters from the string s. The output string should not have any adjacent duplicates.
 

Input:
The first line of input contains an integer T, denoting the no of test cases. Then T test cases follow. Each test case contains a string str.

Output:
For each test case, print a new line containing the resulting string.

Constraints:
1<=T<=100
1<=Length of string<=50

Example:
Input:
2
geeksforgeek
acaaabbbacdddd

Output:
gksforgk
acac"""


def removeDuplicatesUtil(s, start):
    global isDone
    if len(s) <= 1:
        return s
    
    flag = False
    while start < len(s) - 1:
        end = start
        while end < len(s)-1 and s[start] == s[end+1] :
            end = end+1
            flag = True
        if flag == True:
            break
        else:
            start = start + 1
    #print('{} {} {}'.format(s, start, end))   
    
    if start == len(s)-1:
        return s
    else:
        isDone = False
        return removeDuplicatesUtil(''.join([s[:start], s[end+1:]]), end+1 - (end-start+1))
        

t = int(input())
for tc in range(t):
    s = input()
    isDone = False
    while not isDone:
        isDone = True
        s = removeDuplicatesUtil(s, 0)
    print(s)