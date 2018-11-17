# -*- coding:utf-8 -*-
import heapq

class Bonus:
    def getMost(self, board):
        # write code here
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    board[i][j] += board[i][j-1]
                elif j == 0:
                    board[i][j] += board[i-1][j]
                else:
                    temp1 = board[i-1][j]
                    temp2 = board[i][j-1]
                    if temp1 < temp2:
                        board[i][j] += temp2
                    else:
                        board[i][j] += temp1

        return board[-1][-1]

    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 6:
            return index
        result = [1 for _ in range(index)]
        i2 = 0
        i3 = 0
        i5 = 0
        for i in range(index):
            next2 = result[i2] * 2
            next3 = result[i3] * 3
            next5 = result[i5] * 5
            index[i] = min(next2, min(next3, next5))
            if index[i] == next2:
                i2 += 1
            if index[i] == next3:
                i3 += 1
            if index[i] == next5:
                i5 += 1
        return result[index - 1]

    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s or len(s) == 0:
            return -1
        charSet = []
        charDict = {}
        for index,i in enumerate(s):
            if i not in charSet:
                charDict[i] = [1,index]
                charSet.append(i)
            else:
                charDict[i][0] += 1
        for i in charSet:
            if charDict[i][0] == 1:
                return charDict[i][1]


def getLongestStr(s):
    maxLen = 0
    curLen = 0
    stringIndex = [-1 for _ in range(26)]
    for t,i in enumerate(s):
        index = ord(i) - 97
        preIndx = stringIndex[index]
        if preIndx == -1  or t - preIndx > curLen:
            curLen += 1
        else:
            maxLen = max(maxLen, curLen)
            curLen = t - preIndx
        stringIndex[index] = t
    maxLen = max(maxLen,curLen)
    return maxLen

def multiply(A):
    # write code here
    length = len(A)
    B = [0 for _ in range(length)]
    pre = 1
    for i in range(length):
        B[i] = pre
        pre = pre * A[i]
    pre = 1
    for i in range(length):
        index = length - i - 1
        B[index] = B[index] * pre
        pre *= A[index]
    return B


import heapq
class So:

    # def __init__(self):
    #     self.max_heap = []
    #     self.min_heap = []
    #     self.count = 0
    # def Insert(self, num):
    #     # write code here
    #     if self.count % 2 == 0:
    #         heapq.heappush(self.max_heap,-num)
    #         root = heapq.heappop(self.max_heap)
    #         heapq.heappush(self.min_heap,-root)
    #     else:
    #         heapq.heappush(self.min_heap,num)
    #         root = heapq.heappop(self.min_heap)
    #         heapq.heappush(self.max_heap,-root)
    #     self.count += 1
    # def GetMedian(self,data):
    #     # write code here
    #     print self.min_heap,self.max_heap
    #     if  self.count % 2 == 0 :
    #         root1 = self.min_heap[0]
    #         root2 = self.max_heap[0]
    #         return (root1 - root2) / 2.00
    #     else:
    #         return self.min_heap[0]

    def maxInWindows(self, num, size):
        # write code here
        length = len(num)
        if length == 0 or size > length or size <= 0:
            return []
        res = []
        heap = []
        for i in range(size):
            heapq.heappush(heap, -num[i])
        res.append(-heap[0])
        for i in range(1, length - size + 1):
            j = i + size - 1
            heap.remove(-num[i - 1])
            print heap
            heapq.heappush(heap,-num[j])
            res.append(-heap[0])
            print heap
        return res

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        print g
        while i < len(g) and j < len(s):
            if g[i] <= s[i]:
                i += 1
            j += 1

        return i

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        start = 0
        end = length - 1
        k = k -1
        while start < end:
            j = self.partion(nums,start,end)
            if j == k:
                break
            elif j < k:
                start = j + 1
            else:
                end = j -1
        return nums[k]
    def partion(self,nums,start,end):
        i = start
        j = end
        pivot = nums[i]
        while i < j:
            while i < j and nums[j] <= pivot:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] >= pivot:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = pivot
        print nums,i
        return i



class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = {}
        max_time = 1
        for num in nums:
            if num not in freq_dict.keys():
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
                max_time = max(max_time,freq_dict[num])
        num_time = [None]*max_time
        print num_time
        for key in freq_dict.keys():
            freq = freq_dict[key]-1
            if num_time[freq]:
                num_time[freq].append(key)
            else:
                num_time[freq] = [key]
        res = []
        index = 1
        while index < max_time:
            if num_time[-index]:
                res.extend(num_time[-index])
            if len(res) == k:
                break
            index += 1
        return res

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq_dict = {}
        max_freq = 0
        for i in s:
            if i not in freq_dict.keys():
                freq_dict[i] = 1
            else:
                freq_dict[i] += 1
            max_freq = max(max_freq, freq_dict[i])
        times = [None] * max_freq
        print times,max_freq
        for key in freq_dict.keys():
            freq = freq_dict[key] - 1
            if times[freq]:
                times[freq].append(key)
            else:
                times[freq] = [key]
        index = max_freq - 1
        res = ''
        while index >= 0:
            if times[index]:
                for t in times[index]:
                    res += (str(t) * (index + 1))
            index -= 1
        return res

def reverseBits(n):
    n = n & 0xffffffff
    print bin(n)

