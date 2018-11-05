#MaxSubstring  with atmost K occurre
def MaxSubstring(charcode, s, k):
    al = dict(zip(list("abcdefghijklmnopqrstuvwxyz"), list(charcode)))
    print(al)
    lens = len(s)
    maxs = 0
    dp = [[0 for j in range(k+1)] for i in range(lens+1)]
    
    #basecase
    for ib in range(0, lens):
        if al[s[ib]] == '1':
            dp[ib][0] = 1
        else:
            dp[ib][0] = 0
    
    
    for i in range(lens-1, -1, -1):
        for j in range(1, k+1):
            if al[s[i]] == '1':
                dp[i][j] = 1+dp[i+1][j]
            else:
                dp[i][j] = 1+dp[i+1][j-1] 
            
            if dp[i][j] > maxs:
                maxs = dp[i][j]
    return maxs

#driver program
charcode = input().strip()
s = input().strip()
k = int(input())
MaxSubstring(charcode, s, k)