
def getNum(nums):
    if not nums or len(nums) == 1:
        return False
    allsum = sum(nums)
    presum = nums[0]
    for i in range(1,len(nums)-1):
        target = allsum - nums[i]
        if target % 2 != 0:
            presum += nums[i]
            continue
        if target / 2 == presum:
            return nums[i]
        else:
            presum += nums[i]
    return False
# nums = list(map(int,raw_input().split(',')))
# res =  getNum(nums)
# print res

def maxKsum(nums1,nums2,k):
    m = len(nums1)
    n = len(nums2)
    if k > m*n:
        k = m*n
    res = []
    nums1.sort(reverse=True)
    nums2.sort(reverse=True)
    j = 0
    t = nums1[0]
    while len(res) < k and j < n-1:
        i = 0
        sub2 = nums2[j] - nums2[j+1]
        while i < m and t - nums1[i] <= sub2:
            res.append(nums1[i]+nums2[j])
            if len(res) == k:
                return res
            i += 1
        j += 1
    if len(res) < k:
        print j
        for i in range(k-len(res)):
            res.append(nums2[j]+nums1[i])
    return res


# raw = raw_input().split('-')
# num1 = list(map(int,raw[0].split(',')))
# temp = raw[1].split(':')
# num2 = list(map(int,temp[0].split(',')))
# k = int(temp[1])
# res = maxKsum(num1,num2,k)
# res = list(map(str,res))
# print ','.join(res)

def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m = len(word1)
    n = len(word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        dp[i][0] = 3*i
    for i in range(1,n+1):
        dp[0][i] = 3*i
    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                temp1 = min(dp[i-1][j],dp[i][j-1])+3
                temp2 = dp[i-1][j-1]+2
                dp[i][j] = min(temp1,temp2)
    print dp
    return dp[-1][-1]

print minDistance('abc','321')