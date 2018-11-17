import sys


def printMatrix(matrix):
    # write code here
    if not matrix:
        return None
    rows = len(matrix) - 1
    cols = len(matrix[0]) - 1
    i = 0
    j = 0
    result = []
    while (i <= rows and j <= cols):
        for t in range(j, cols + 1):
            result.append(matrix[i][t])
        for t in range(i + 1, rows + 1):
            result.append(matrix[t][cols])
        if i != rows:
            for t in range(cols - 1, j - 1, -1):
                result.append(matrix[rows][t])
        if j != cols:
            for t in range(rows - 1, i, -1):
                result.append(matrix[t][j])
        i += 1
        j += 1
        rows -= 1
        cols -= 1
    return result


# m,n = map(int,raw_input().split())
# nums = []
# for i in range(m):
#     temp = raw_input().split()
#     nums.append(temp)
# stop = raw_input()
# res = printMatrix(nums,m,n)
# res = ','.join(res)
# sys.stdout.write(res)
def  compareVersionNumber(s1,s2):
    s1 = s1.split('.')
    s2 = s2.split('.')
    m = min(len(s1),len(s2))
    for i in range(m):
        if int(s1[i]) > int(s2[i]):
            return 1
        elif int(s1[i]) < int(s2[i]):
            return -1
        else:
            if i == (m-1):
                if len(s1) == len(s2):
                    return 0
                elif len(s1) > m:
                    return 1
                else:
                    return -1
            else:
                continue

def mouseEscape(grid,n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(n):
        for j in range(n):
            if i == 0 and j > 0:
                dp[i][j] = dp[i][j-1]+grid[i][j]
            elif i > 0 and j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            elif i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]

# n = int(raw_input())
# nums = []
# for i in range(n):
#     temp = list(map(int,raw_input().split(',')))
#     nums.append(temp)
# print mouseEscape(nums,n)
m,n = map(int,raw_input().split())
nums = []
for i in range(m):
    temp = raw_input().split()
    nums.append(temp)
stop = raw_input()
res = printMatrix(nums)
res = ','.join(res)
print str(res)+"\n"
