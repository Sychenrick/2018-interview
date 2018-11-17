
def getmaxlen(s):
    if not s:
        return 0
    maxlen = 0
    curlen = 0
    dp = [-1 for _ in range(26)]
    for i in range(len(s)):
        index= ord(s[i])-ord('a')
        pre = dp[index]
        if pre == -1 or i - pre > curlen:
            curlen += 1
        else:
            maxlen = max(maxlen,curlen)
            curlen = i - pre
        dp[index] = i
    return max(curlen,maxlen)

directions = [[0,1],[0,-1],[1,0],[-1,0]]
# def dfs(grid,i,j,m,n):
#     if i < 0 or j < 0 or i >= m  or j >= n or grid[i][j] == '0':
#         return
#     grid[i][j] = '0'
#     for d in directions:
#         dfs(grid,i+d[0],j+d[1],m,n)
# def numteam(grid):
#     if not grid:
#         return 0
#     m = len(grid)
#     n = len(grid[0])
#     num = 0
#     for i in range(m):
#         for j in range(n):
#             if grid[i][j] != '0':
#                 dfs(grid,i,j,m,n)
#                 num += 1
#     return num

def dfs(k,temp,res,s):
    if k == 4 or len(s) == 0:
        if k == 4 and len(s) == 0:
            res.append('.'.join(temp))
    for i in range(len(s)):
        if i != 0 and s[0] == '0':
            break
        part = s[0:i+1]
        if int(part) < 255:
            temp.append(part)
            dfs(k+1,temp,res,s[i+1:])
            temp.pop()

def mostpop(grid,n):
    if not grid:
        return 0
    num = 0
    for i in range(n):
        visited = [0 for _ in range(n)]
        visited[i] = 1
        temp = grid[i]
        for per in temp:
            visited[per] = 1
            for another in grid[per]:
                if visited[another] == 1:
                    continue
                else:
                    visited[another] = 1
        if sum(visited) == n:
            num += 1
    return num
# n = int(raw_input())
# m = int(raw_input())
# res = list(map(int,raw_input().split()))
# grid = [[0 for _ in range(n)] for _ in range(n)]
#
# while len(res):
#     count = 2
#     temp1 = []
#     while count > 0:
#         index = res.pop()
#         temp1.append(index-1)
#         count -= 1
#     grid[temp1[0]][temp1[1]] = 1
#
#
# print mostpop(grid,n)

def utfstring(nums,n):
    if n < 1 or n > 4:
        return 0
    if n == 1:
        return nums[0] <= 127
    if n <= 4:
        for i in range(n):
            if i == 0:
                maxnum = 255 - 2 **(7-n)
                minnum = 0
                temp = n
                index = 7-n
                while temp > 0:
                    minnum += 2 ** (index+temp)
                    temp -= 1

                if nums[i] > maxnum or nums[i] < minnum:
                    return  0

            else:
                if nums[i] > 191 or nums[i] < 128:
                    return 0
    return 1
count = 0
start = 7
while 255 >> start & 1:
    count += 1
    start -= 1
    if start < 0:
        break
print count,start
def si(prices):
    n = len(prices)
    buy = [ 0 for _ in range(n)]
    s1 = [ 0 for _ in range(n)]
    sell = [ 0 for _ in range(n)]
    s2 = [[ 0 for _ in range(n)]]
    s1[0] = buy[0] = -prices[0]
    sell[0] = s2[0] = 0
    for i in range(1,n):
        buy[i] = s2[i-1] - prices[i]
        s1[i] = max(buy[i-1],s1[i-1])
        sell[i] = max(buy[i-1],s1[i-1])+prices[i]
        s2[i] = max(s2[i-1],sell[i-1])
    return max(sell[-1],s2[-1])