"""Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1′ into ‘str2′.

Insert
Remove
Replace
All of the above operations are of cost=1.
Both the strings are of lowercase.

Input:
The First line of the input contains an integer T denoting the number of test cases. Then T test cases follow. Each tese case consists of two lines. The first line of each test case consists of two space separated integers P and Q denoting the length of the strings str1 and str2 respectively. The second line of each test case coantains two space separated strings str1 and str2 in order.


Output:
Corresponding to each test case, pirnt in a new line, the minimum number of operations required.

Constraints:
1<=T<=50
1<= Length(str1) <= 100
1<= Length(str2) <= 100
 

Example:
Input:
1
4 5
geek gesek

Output:
1"""
    def editDistance(dp, str1, str2, l1, l2):
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return dp[l1][l2]

    t = int(input())
    for tc in range(t):
        l1, l2 = map(int, input().strip().split())
        str1, str2 = input().strip().split()
        dp = [[0 for j in range(l2+1)] for i in range(l1+1)]

        if l1 >= l2:
            grt = l1
        else:
            grt = l2

        for val in range(grt+1):
            if val <= l1:
                dp[val][0] = val

            if val <= l2:
                dp[0][val] = val

        for i in range(l1+1):
            print(dp[i])

        print(editDistance(dp, str1, str2, l1, l2))
        print()
        for i in range(l1+1):
            print(dp[i])