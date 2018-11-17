
def getNum(temp):
    result = 0
    m = temp[0]
    n = temp[1]
    if n == 1 and m == 1:
        result = 1

    elif n == 1:
        result = m - 2
    elif m == 1:
        result = n - 2
    else:
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n-1:
                    continue
                else:
                    result += 1
    print result

n,m = map(int,raw_input().split())
init = int(raw_input())
res = [0 for _ in range(n)]
for i in range(m):
    temp = list(map(int,raw_input().split()))
    index = temp[1] -1
    if temp[0] == 2:
        res[index] += temp[2]

        while res[index] > init:
            more = res[index] - init
            res[index] = init
            index = index - 1
            if index < 0:
                break
            res[index] += more

    else:
        print res[index]


def findIntegers(self, num):
    """
    :type num: int
    :rtype: int
    """
    dp = [0 for _ in range(31)]
    dp[0] = 1
    dp[1] = 2
    for i in range(2, 31):
        dp[i] = dp[i - 2] + dp[i - 1]
    k = 31
    res = 0
    pre = 0
    while k >= 0:
        if (num & (1 << k)):
            res += dp[k]
            if pre:
                return res
            pre = 1
        else:
            pre = 0
        k -= 1
    return res + 1
