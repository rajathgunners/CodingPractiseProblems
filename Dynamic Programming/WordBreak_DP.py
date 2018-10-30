"""Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" or "i like sam sung".

Input:
First line is integer T denoting number of test cases. 1<=T<=100.
Every test case has 3 lines.
First line is N number of words in dictionary. 1<=N<=12.
Second line contains N strings denoting the words of dictionary. Length of each word is less than 15.
Third line contains a string S of length less than 1000.

Output:
Print 1 is possible to break words, else print 0.

Example:
Input:
2
12
i like sam sung samsung mobile ice cream icecream man go mango
ilike
12
i like sam sung samsung mobile ice cream icecream man go mango
idontlike
Output:
1
0"""
def WordBreak(wl, s, N):
    
    dp = [[9 for a in range(N+1)] for b in range(N+1)]
    
    dp[0][0] = 1
    for k in range(1, N+1):
        dp[0][k] = 0
        dp[k][0] = 0
    
    for i in range(1,N+1):
        flag = 0
        for j in range(i, N+1):
            dp[i][j] = int((dp[i-1][i-1] and (s[i-1:j] in wl)) or dp[i-1][j])
            
            if dp[i][j]:
                flag = 1
        
        if dp[i-1][i-1] and dp[i][N]:
            #for x in range(1, N+1):
                #print(dp[x][1:])
            return 1
        
        if flag == False:
            #for x in range(1, N+1):
                #print(dp[x][1:])
            return 0
    
            
    

t = int(input())
for tc in range(t):
    M = int(input())
    wl = input().strip().split()
    s = input()
    print(WordBreak(wl, s, len(s)))
