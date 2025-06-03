# LONGEST COMMOM SUBSEQUENCE UING RECURSION

def lcs(s1,s2,i,j):
    if i==0 or j==0:
        return 0
    if s1[i-1]==s2[j-1]:
        return 1+lcs(s1,s2,i-1,j-1)
    else:
        return max(lcs(s1,s2,i-1,j),lcs(s1,s2,i,j-1))
s1="abcd"
s2="abce"
print(lcs(s1,s2,len(s1),len(s2)))


# USING TABULATION

'''
#S1=abaaba
#S2=babbab

   0  b  a  b  b  a  b

0  0  0  0  0  0  0  0

a  0  0  1  1  1  1  1

b  0  1  1  2  2  2  2

a  0  1  2  2  2  3  3 

a  0  1  2  2  2  3  3

b  0  1  2  3  3  3  4

a  0  1  2  3  3  4  4
'''

s1="abaaba"
s2="babbab"
n,m=len(s1),len(s2)
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])

# PRINT LENGTH OF LARGEST COMMEM SUBSEQUENCE

s1="abaaba"
s2="babbab"
n,m=len(s1),len(s2)
dp=[[""]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+s1[i-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(len(dp[n][m]))
print(dp[n][m])


# coins
coins=[1,2,5]
amount=11
dp=[float('inf')]*(amount+1)
dp[0]=0
for coin in coins:
    for i in range(coin,amount+1):
        dp[i]=min(dp[i],dp[i-coin]+1)
if dp[amount]!=float('inf'):
    print(dp[amount])
else:
    print(-1)
        
