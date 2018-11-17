def getMaxNum(n):
    if not n:
        return 0
    list_string = list(str(n))
    cnt = 0
    temp = 0
    for i in list_string:
        temp += int(i)
        if temp % 3 == 0:
            cnt += 1
            temp = 0

    return cnt


def indexY(x,k):
    cnt = 0
    y = 1
    while True:
        if x & y == 0:
            cnt += 1
            if cnt == k:
                return y
        y += 1


def getALl(indexList):
    if len(indexList) == 0:
        return
    dp = [[] for _ in range(len(indexList))]
    dp[0] = ['',indexList[0]]
    for i in range(1,len(indexList)):
        dp[i] = []
        for t in dp[i-1]:
            dp[i].append(t)
            dp[i].append(t+str(indexList[i]))
    return dp[-1]

def printAllString(prob):
    if len(prob) == 0:
        return
    dp = [[] for _ in range(len(prob))]
    if prob[0] == 1:
        dp[0].append(str(0))
    else:
        dp[0] = ['',str(0)]
    for i in range(1,len(prob)):
        if prob[i] == 1:
            for t in dp[i-1]:
                dp[i].append(t+str(i))
        else:
            for t in dp[i-1]:
                dp[i].append(t)
                dp[i].append(t+str(i))
    return sorted(dp[-1])

def getMax(nums):
    if not nums:
        return 0
    length = len(nums)
    if length == 0:
        return 0
    dp = [0 for _ in range(length)]
    sum = 0
    for i in range(length):
        for j in range(0,i):
            if nums[i] > nums[j]:
                sum = max(sum,dp[j])
        dp[i] = sum + nums[i]
    return max(dp)


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        longest = ''
        for string in d:
            len1 = len(longest)
            len2 = len(string)
            if len1 > len2 or (len1 == len2 and longest < string):
                continue
            if self.isValid(s, string):
                longest = string
            print longest
        return longest

    def isValid(self, s, target):
        i = 0
        j = 0
        while i < len(s) and j < len(target):
            if s[i] == target[j]:
                j += 1
            i += 1
        return j == len(target)


if __name__ == "__main__":
    s = Solution()
    r = "abpcplea"
    t = ["a", "b", "c"]
    print s.findLongestWord(r,t)