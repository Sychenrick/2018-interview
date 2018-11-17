

# raw = raw_input().split(':')
# carry = raw[2][2:]
# raw[2] = raw[2][0:2]
# if carry == 'PM':
#     if raw[0] != '12':
#         raw[0] = str(int(raw[0])+12)
#     print ':'.join(raw)
# else:
#     if raw[0] == '12':
#         raw[0] = '00'
#     print ':'.join(raw)

# t = int(raw_input())
# def getTimenum(T):
#     temp = T
#     cnt = 0
#     while T > 0:
#         T -= 3*(2**cnt)
#         cnt += 1
#     res = 3*(2**cnt) - temp -2
#
#     return res
# print getTimenum(t)

from collections import defaultdict
def getMaxlen(nums,k):
    numdict= defaultdict(int)
    for i in range(len(nums)):
        temp = nums[i] % k
        numdict[temp] += 1
    res = sorted(numdict.items(),key=lambda x:x[1],reverse=True)
    maxlen = 0
    for num in res[0:-1]:
        maxlen += num[1]

    print maxlen
N,K = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
getMaxlen(nums,K)
