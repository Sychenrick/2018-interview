





def minLength(s,k):
    res = []
    for index,i in enumerate(s):
        if i == '0':
            res.append(index)
    res.append(len(s))
    print res
    if k >= len(res) -1:
        return len(s)
    temp = 0
    for i in range(k,len(res)):
        temp = max(temp,res[i]-res[i-k])
    return  temp



def dfs(graph, i, marked):
    maxdeepth = 0
    marked[i] = 1
    for num in graph[i]:
        if marked[num]:
            continue
        marked[num] = 1
        temp = 1 + dfs(graph, num, marked)
        maxdeepth = max(maxdeepth, temp)
        marked[num] = 0
    return maxdeepth

def minNum(nums):
    nums.sort()
    num = 1
    pre = nums[0]
    res = 0
    for i in range(1,len(nums)):
        num  = num % 3
        if (nums[i] - pre) <= 10:
            num += 1
        else:
            res += (3-num)
            num = 1
        pre = nums[i]
    return res+(3-num)




if __name__ == '__main__':
    n = int(raw_input())
    nums = list(map(int, raw_input().split()))
    print minNum(nums)
res.append()