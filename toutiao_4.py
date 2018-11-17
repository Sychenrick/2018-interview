

def sumKTarget(nums,target,k,res,temp):
    if target < 0 or k < 0 or (target > 0 and k < 0):
        return
    if len(temp) == k and target == 0:
        res.add(tuple([i for i in temp]))
        return
    for num in nums:
        cur = target - num
        temp.append(num)
        sumKTarget(nums,cur,k,res,temp)
        temp.pop()


# a,b,k = map(int,raw_input().split())
# if a > b:
#     a,b = b,a
# nums = [a,b]
# res = set()
# temp = []
# sumKTarget(nums,a,k,res,temp)
# temp = []
# sumKTarget(nums,b,k,res,temp)
# print res
# print int(len(res) % (1e9+7))
import sys
def mostLevel(coins,N,costs,levels):
    dp = [[0 for _ in range(coins+1)] for _ in range(N+1)]
    for i in range(1,N+1):
        cost = costs[i]
        level = levels[i]
        for j in range(1,coins+1):
            if j >= cost:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-cost]+level)
            else:
                dp[i][j] = dp[i-1][j]


    return dp[N][coins]

coins = int(raw_input())
n = int(raw_input())
costs = []
levels = []
line = sys.stdin.readline().strip()
temp = list(map(int, line.split()))
costs.append(temp[0])
levels.append(temp[1])
while True:
    line = sys.stdin.readline().strip()
    if not line or line is None:
        break
    temp = list(map(int, line.split()))
    costs.append(temp[0])
    levels.append(temp[1])
res = mostLevel(coins,n,costs,levels)
print res

def climb(n,a,b,nums):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(n+1):
        if i in nums:
            dp[i] = 0
            continue
        for j in range(a,b+1):
            temp = i - j
            if temp >= 0 and temp not in nums:
                dp[i] += dp[i-j]
    print dp
    return dp[-1]
# n = int(raw_input())
# a = int(raw_input())
# b = int(raw_input())
# m = int(raw_input())
# nums = set()
# for i in range(m):
#     nums.add(int(raw_input()))
#
#
# res = climb(n,a,b,nums)
# print int(res% (1e9+7))