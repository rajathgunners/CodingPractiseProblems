"""Given an array of integers A and a sum B, find all unique combinations in A where the sum is equal to B. The same repeated number may be chosen from A unlimited number of times.
Note:
All numbers will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
If there is no combination possible the print "Empty" (without qoutes).
Example,
Given A = 2,4,6,8 and B(sum) = 8,
A solution set is:

[2, 2, 2, 2]
[2, 2, 4]
[2, 6]
[4, 4]
[8]

Input:
First is T , no of test cases. 1<=T<=500
Every test case has three lines.
First line is N, size of array. 1<=N<=12
Second line contains N space seperated integers(x). 1<=x<=9.
Third line is the sum B. 1<=B<=30.
 
Output:
One line per test case, every subset enclosed in () and in every set intergers should be space seperated.(See example)

Example:
Input:
3
4
7 2 6 5
16
11
6 5 7 1 8 2 9 9 7 7 9
6
4
5 2 2 6
3

Output:
(2 2 2 2 2 2 2 2)(2 2 2 2 2 6)(2 2 2 5 5)(2 2 5 7)(2 2 6 6)(2 7 7)(5 5 6)
(1 1 1 1 1 1)(1 1 1 1 2)(1 1 2 2)(1 5)(2 2 2)(6)
Empty"""


def myPrint(x):
    return '(' + ' '.join(map(str, x)) + ')'

def combinationSum(ln, temp, sums):
    global finallist
    if sums == 0:
        if temp not in finallist: 
            finallist.append(temp)
        return 
    elif sums < 0 or not ln:
        return 
    else:
        if sums < ln[0]:
            combinationSum(ln[1:], temp, sums)
        else:
            combinationSum(ln, temp + [ln[0]], sums-ln[0])
            combinationSum(ln[1:], temp, sums)
            


t = int(input())
for tc in range(t):
    n = int(input())
    ln = map(int, input().strip(' ').split(' '))
    ln = sorted(ln)
    sums = int(input())
    finallist = list()
    combinationSum(ln, [], sums)
    if finallist:
        finallist = map(myPrint, finallist)
        for fl in finallist:
            print(fl, end='')
    else:
        print('Empty')
    print()