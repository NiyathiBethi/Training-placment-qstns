# FIBONACCI SERIES USING RECURSION

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
x=int(input())
print(fib(x))
 

# FIBONACCI SERIES USING DYNAMIC PROGRAMMING--TIME COMPLEXITY--O(n), SPACE COMPLEXITY--O(2n)
# MEMOIZATION(TOP DOWN APPROACH)

n=6
memo=[-1]*(n+1)
def fib(n):
    if n==1 or n==0:
        return n
    if memo[n]!=-1:
        return memo[n]
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
print(fib(n))

#TABULATION(BOTTOM UP) TIME COMPLEXITY--O(n),SPACE COMPLEXITY--O(n)

n=6
dp=[-1]*(n+1)
dp[1]=1
dp[0]=0
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])

#OPTIMIZED CODE
# TIME COMPLEXITY--O(n),SPACE COMPLEXITY--O(1)

n=6
a,b=0,1
for _ in range(2,n+1):
    fib=a+b
    a=b
    b=fib
print(fib)

'''
How to solve:
→Convert the problem in terms of indices
→Do all the possible operations on the index
→ Count all ways: Find the sum
→ Max Output: Find the max
→ Min Output: Find the min
'''
# 70. Climbing Stairs--LEET CODE

# f(ind)
# f(ind==0)
# return 1
# j1=f(ind-1)--step-1
# j2=(ind-2)--step-2
# return j1+j2--step-3

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==2:
            return 2
        if n==1:
            return 1
        p1=2
        p2=1
        c=0
        for i in range(2,n):
            c=p1+p2
            p2=p1
            p1=c
        return c

# 403. Frog Jump-- LEET CODE
#TIME COMPLEXITY(Recursion)--O(2n)

# f(ind)
# if(ind==0)return
# j1=f(ind-1)+abs((a[ind])-a[ind-1])
#if(ind<1)--> j2=f(ind-2)+abs((a[ind])-a[ind-2])
# return min(j1,j2)

def frog(ind):
    if ind==0:
        return 0
    j1=frog(ind-1)+abs(rock[ind]-rock[ind-1])
    if ind>1:
        j2=frog(ind-2)+abs(rock[ind]-rock[ind-2])
        return min(j1,j2)
    else:
        return j1
rock=[0,1,3,5,6,8,12,17]
print(frog(len(rock)-1))

# FROG JUMP USING MEMOIZATION

def frog(ind,memo):
    if ind==0:
        return 0
    if memo[ind]!=-1:
        return memo[ind]
    j1=frog(ind-1,memo)+abs(rock[ind]-rock[ind-1])
    if ind>1:
        j2=frog(ind-2,memo)+abs(rock[ind]-rock[ind-2])
        memo[ind]=min(j1,j2)
        return memo[ind]
    else:
        memo[ind]=j1
    return memo[ind]
rock=[30,10,60,10,60,50]
n=len(rock)
memo=[-1]*(n+1)
print(frog(n-1,memo))

        
# FROG JUMP USING TABULATION

rock=[30,10,60,10,60,50]
n=6
dp=[0]*n
for i in range(1,n):
    j1=dp[i-1]+abs(rock[i]-rock[i-1])
    j2=float('inf')
    if i>1:
        j2=dp[i-2]+abs(rock[i]-rock[i-2])
        dp[i]=min(j1,j2)
print(dp[n-1])


# COIN CHANGE

arr=[1,2,5,10]
target=12
n=len(arr)
dp=[[False]*(target+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=True
for i in range(1,n+1):
    for j in range(1,target+1):
        if arr[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
if dp[n][target]:
    print("Yes")
else:
    print("No")