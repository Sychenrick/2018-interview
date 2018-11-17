import operator

def getSer(inputString):
    resdict = {}
    for i in range(len(inputString)):
        if inputString[i] in resdict:
            resdict[inputString[i]] += 1
        else:
            resdict[inputString[i]] = 1
    resdict = sorted(resdict.items(),key=operator.itemgetter(0))
    res = ''
    for temp in resdict:
        res = res + temp[0]+str(temp[1])
    return res

def step(n):
    if n == 0:
        return 0
    if n <= 3:
        return n
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    count = 2
    for i in range(4,n+1):
        if 2**(count+1) <= i:
            count += 1
        for j in range(count+1):
            dp[i] += dp[i-2**j]

    return dp[-1] % (10**9+3)

# m = int(raw_input())
# for i in range(m):
#     n = int(raw_input())
#     print step(n)

def maxSubSum(nums,m):
    if not nums:
        return 0
    maxsum = 0
    presum = 0
    start = 0
    end = len(nums)
    for i in range(len(nums)):
        if presum <= 0:
            presum = nums[i]
            if i < end:
                start = i
        else:
            presum += nums[i]
        if presum > maxsum:
            maxsum = presum
            end = i
    if start == end:
        nums.pop(start)
    else:
        nums = nums[:start] + nums[end+1:]
    return maxsum,nums

def getPostive(nums):
    count = 0
    cursum = 0
    if nums[0] > 0:
        cursum = nums[0]
    if nums[-2] < 0:
        count = 1
    for i in range(1,len(nums)):
        if nums[i] < 0 and nums[i-1] > 0:
            count += 1
        if nums[i] > 0:
            cursum += nums[i]

    return count,cursum
n,m = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
postiveNum,tempsum = getPostive(nums)
if m >= postiveNum:
    print tempsum,postiveNum
else:
    res = 0
    res = maxSubSum(nums,m)
    print res



