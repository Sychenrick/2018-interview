# k = int(raw_input())
# s1 = raw_input()
# s2 = raw_input()


def getSubstr(s,k):
    if not s:
        return
    length = len(s)
    res = set()
    for i in range(length-k+1):
        res.add(s[i:i+k])
    return res

def countNum(s1,s2,k):
    s1substr = getSubstr(s1,k)
    cnt = 0
    for i in range(len(s2)-k+1):
        s = s2[i:i+k]
        if s in s1substr:
            cnt += 1
    return cnt

import math
# Q,M = map(int,raw_input().split())
# allsum = (Q + M)*2
# N = int(math.sqrt(allsum))
def getMin(score,n,maxsum):
    if score > maxsum:
        return -1
    if score <= n:
        return 1
    for i in range(n,0,-1):
        temp = score
        curmax = i
        cnt = 0
        while temp > 0 and curmax > 0:
            sub = temp - curmax
            if sub < 0:
                curmax -= 1
            elif sub >= 0 and sub < curmax:
                cnt += 1
                return cnt+1
            else:
                temp = sub
                curmax -= 1

    return -1


import itertools
def traNum(a,b,c):
    cnt = 0
    for i in range(1,a+1):
        for j in range(1,b+1):
            maxnum = min(c+1,i+j)
            minnum = max(0,abs(i-j))
            for t in range(minnum+1,maxnum):
                print i,j,t
                cnt += 1
    return cnt
X,Y,Z = map(int,raw_input().split())
print traNum(X,Y,Z)



