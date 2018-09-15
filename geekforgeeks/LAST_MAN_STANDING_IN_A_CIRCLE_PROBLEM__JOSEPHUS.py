#LAST_MAN_STANDING_IN_A_CIRCLE_PROBLEM 
"""Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle in a fixed direction.​ The task is to choose the safe place in the circle so that when you perform these operations starting from 1st place in the circle, you are the last one remaining and survive. You are required to complete the function josephus which returns an integer denoting such position . 

Input:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow. Each test case contains 2 integers n and k .

Output:
For each test case in a new line output will be the safe position which satisfies the above condition.

Constraints:
1<=T<=100
1<=k,n<=20

Example(To be used only for expected output) :
Input:
2
3 2
5 3

Output
3
4
"""
def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n-1, k) + k-1)%n + 1

print(josephus(5, 3))
        
        