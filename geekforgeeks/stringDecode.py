""" An encoded string (s) is given, the task is to decode it. The pattern in which the strings were encoded were as follows
original string: abbbababbbababbbab 
encoded string : "3[a3[b]1[ab]]".

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains a string s.

Output:
For each test case in a new line print the required decoded string.

Constraints:
1<=T<=10
1<=length of the string <=30

Example:
Input:
2
1[b]
3[b2[ca]]

Output:
b
bcacabcacabcaca """"
def stringDecode(ip):
    stack = list()
    pos = 0
    while pos < len(ip):
        if ip[pos].isdecimal():
            if ip[pos+1].isdecimal():
                stack.append(int(ip[pos:pos+2]))
                pos = pos+1
            else:
                stack.append(int(ip[pos:pos+1]))
        elif ip[pos] is ']':
            temp = []
            while stack:
                if stack[-1] == '[':
                    stack.pop()
                    stack[-1] = ''.join(stack[-1]*temp)
                    #print(stack)
                    break
                else:
                    temp.insert(0,stack.pop())
        else:
            stack.append(ip[pos:pos+1])
        pos = pos+1
    print(stack[0])


stringDecode("3[a3[b]1[ab]]")
print()
stringDecode("1[b]")
print()
stringDecode("3[b2[ca]]")