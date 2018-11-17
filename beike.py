


def getNum(n,m,start,res,temp):
    if len(temp) == n-1:
        if m % temp[-1] == 0:
            res.append([i for i in temp])
            return
        else:
            return
    for i in range(start,m+1):
        if len(temp):
            pre = temp[-1]
        else:
            pre = 1

        if i % pre == 0:
            temp.append(i)
            getNum(n,m,start,res,temp)
            temp.pop()

res = []
temp = []
n,m = map(int,raw_input().split())
getNum(n,m,1,res,temp)
print int(len(res)%(1e9+7))

import sys

from math import sqrt


def isPrime(num):
    if num == 2 or num == 3:
        return True
    if num % 6 != 1 and num % 6 != 5:
        return False
    tmp = int(sqrt(num))
    for i in range(5, tmp + 1):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def texNum(n):
    if n == 2:
        return 1
    if n % 2 == 0:
        return 2
    if isPrime(n):
        return 1
    else:
        return 3

# first = sys.stdin.readline().strip()
# res = texNum(int(first[0]))
# print res
# while True:
#     first = sys.stdin.readline().strip()
#     if not first or first is None:
#         break
#     res = texNum(int(first[0]))
#     print res



def seriesNum(m):
    temp = []
    for i in range(1,m+1):
        if m % i == 0:
            temp.append(i)
    temp.sort()
    return temp

def getNum(n,start,select,temp):
    global res
    if len(temp) >= n:
        return
    if len(temp) == n-1:
        res += 1
        return
    for i in range(start,len(select)):
        temp.append(select[i])
        getNum(n,i,select,temp)
        temp.pop()
n,m = map(int,raw_input().split())
select = seriesNum(m)
res = 0
temp = []
getNum(n,0,select,temp)
print int(res%(1e9+7))