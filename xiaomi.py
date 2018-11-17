
def binarySearch(nums,start,end,key):
    if start > end:
        return
    i = start
    j = end
    while i <= j:
        print i
        mid = i + (j-i) / 2
        temp = nums[mid]
        if temp == key:
            return mid
        elif temp < key:
            i = mid + 1
        else:
            j = mid - 1
    return i

def firstLarget(nums,key):
    index = binarySearch(nums,0,len(nums)-1,key)
    print index
    # if nums[index] == key and index >= len(nums)-1:
    #     return -1
    # elif nums[index] == key:
    #     return nums[index+1]
    # else:
    #     return nums[index]

firstLarget([1,3,5,7,8,9],6)

def miHomeGiftBag(nums, target):
    if target == 0:
        return 1
    if target < 0 or (len(nums) == 0 and target != 0):
        return 0
    for i in range(len(nums)):
        temp = target - nums[i]
        if miHomeGiftBag(nums[i+1:],temp):
            return 1
    return 0


# n = int(raw_input())
# nums = list(map(int,raw_input().split()))
# target = int(raw_input())
# nums.sort()
# res = miHomeGiftBag(nums,target)
# print res

maxavg = []
def splitList(nums,m,res):
    n = len(nums)
    if m > n:
        return 0
    if m == n:
        res.append(max(nums))
        return max(res)
    if m == 1:
        res.append(sum(nums))
        return max(res)
    for i in range(len(nums)-m+1):
        res.append(sum(nums[0:i+1]))
        if splitList(nums[i+1:],m-1,res):
            maxavg.append(max(res))
            res = []

# n,m = map(int,raw_input().split())
# nums = list(map(int,raw_input().split()))
# res = splitList(nums,m,n)
# print res
res = []
splitList([10,7,9,3,5,6],4,res)
print maxavg

