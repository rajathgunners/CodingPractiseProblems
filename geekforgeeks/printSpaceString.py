"""Given a string str your task is to complete the function printSpaceString which takes only one argument the string str and  prints all possible strings that can be made by placing spaces (zero or one) in between them. 

For eg .  for the string abc all valid strings will be
                abc
                ab c
                a bc
                a b c


Input:
The First line of input takes an integer T denoting the number of test cases . Then T test cases follow . Each line of test case contains a string str .

Output:
For each test case output the strings possible in a single line  separated by a "$" 

Constraints:
1<=T<=100
1<=length of string str <=100

Example:
Input
1
abc

Output
abc$ab c$a bc$a b c$"""

def printSpaceUtil(str1, str2, const):
    if str1 == '':
        return
    else:
        if len(str2) < 2:
            if const == '':
                if str2 == '':
                    print('{}'.format(str1), end='$')
                else:
                    print('{} {}'.format(str1, str2), end='$')
            else:
                if str2 == '':
                    print('{} {}'.format(const, str1), end='$')
                else:
                    print('{} {} {}'.format(const, str1, str2), end='$')
        else:
            #print('{} {} {}'.format(const, str1, str2), end='$')
            if const == '':
                printSpaceUtil(str2, '', str1)
            else:
                printSpaceUtil(str2, '', const + ' ' + str1)
        str2 = str1[-1]+str2
        str1 = str1[:-1]
        printSpaceUtil(str1, str2, const)
            

#testcall
printSpace(input("print enter input :\t"), '', '')