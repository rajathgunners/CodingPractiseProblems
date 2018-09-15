
"""Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "snakesandladder",
dict = ["snake", "snakes", "and", "sand", "ladder"].

A solution is ["snakes and ladder",
           "snake sand ladder"].

Input:
The first line contains an integer T, denoting the number of test cases.
Every test case has 3 lines.
The first line contains an integer N, number of words in the dictionary.
The second line contains N strings denoting the words of the dictionary.
The third line contains a string s.

Output:
For each test case, print all possible strings in one line. Each string is enclosed in (). See Example.
If no string possible print "Empty" (without quotes).

Constraints:
1<=T<=100
1<=N<=20
1<=Length of each word in dictionary <=15
1<=Length of s<=1000
 

Note: Make sure the strings are sorted in your result.

Exapmle:
Input:
1
5
lr m lrm hcdar wk
hcdarlrm

Output:
(hcdar lr m)(hcdar lrm)"""

finallist = list()
def myPrint(x):
    return '(' + ' '.join(x) + ')'


def wordBreakTest(s, lw, ls):
    if len(s) == 0:
        finallist.append(ls)
        return 
    #matchList = list()
    for l in lw:
        if s.find(l) == 0:
            t = len(l)
            wordBreakTest(s[t:], lw, ls+[l])
    
    return

t = int(input())
for tc in range(t):
    n = int(input())
    glw = input().strip(' ').split(' ')
    s = input()
    finallist = list()
    wordBreakTest(s, glw, [])
    if finallist:
        finallist = map(myPrint, finallist)
        for fl in finallist:
            print(fl, end='')
    else:
        print('Empty')
    
           
    