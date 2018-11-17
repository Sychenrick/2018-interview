#
# def InversePairs(data):
#     if not data:
#         return 0
#     temp = [i for i in data]
#     return mergeSort(temp, data, 0, len(data) - 1)
#
# def mergeSort(temp, data, low, high):
#     if low >= high:
#         temp[low] = data[low]
#         return 0
#     mid = (low + high) / 2
#     left = mergeSort(data, temp, low, mid)
#     right = mergeSort(data, temp, mid + 1, high)
#
#     count = 0
#     i = low
#     j = mid + 1
#     index = low
#     while i <= mid and j <= high:
#         if data[i] <= data[j]:
#             temp[index] = data[i]
#             i += 1
#         else:
#             temp[index] = data[j]
#             count += mid - i + 1
#             j += 1
#         index += 1
#     while i <= mid:
#         temp[index] = data[i]
#         i += 1
#         index += 1
#     while j <= high:
#         temp[index] = data[j]
#         j += 1
#         index += 1
#     return count + left + right
#
# def countNum(nums,target):
#     if not nums:
#         return 0
#     cnt = 0
#     for num in nums:
#         if num < target:
#             cnt += 1
#     return cnt
#
# def minDamage(nums):
#     raw = [i for i in nums]
#     rawcnt = InversePairs(nums)
#     mincnt = -float('inf')
#     index = 0
#     for i in range(len(nums)):
#         lcnt = countNum(raw[0:i],raw[i])
#         rcnt = countNum(raw[i+1:],raw[i])
#         if rcnt - lcnt > mincnt:
#             mincnt = rcnt-lcnt
#             index = i
#
#     return rawcnt-mincnt,index+1
#
#
# n = int(raw_input())
# nums = list(map(int,raw_input().split()))
#
# res,index = minDamage(nums)
# print str(res) + ' ' + str(index)

n = int(raw_input())
res = [0 for _ in range(n)]
for i in range(n):
    t,info = map(int,raw_input().split())
    if t == 1:
        res[info-1] = 1
    else:
        res[info-1] = 2

def judge(nums):
    tre = nums.count(1)
    fa = nums.count(2)
    if fa < tre:
        print str(0) + ' ' + str(fa)
    else:
        print str(tre) + ' ' + str(fa)
