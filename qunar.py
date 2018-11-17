def minstep(nums,start,temp):
    global res
    if start >= len(nums)-1:
        if len(temp) < len(res):
            res = [i for i in temp]
        return
    cur = nums[start]
    maxval = min(start+cur+1,len(nums))
    for i in range(start+1,maxval):
        temp.append(i-start)
        minstep(nums,i,temp)
        temp.pop()



temp = []
#nums = list(map(int,raw_input().split()))
nums = [2,3,1,1,4]
res = [ 1 for _ in nums]
minstep(nums,0,temp)
minlen = float('inf')
# result = []
# for t in res:
#     if len(t) < minlen:
#         minlen = len(t)
#         result = t
print  ' '.join(map(str,res))

def payAA(paylist,ave):
    items = paylist
    for item in items:
        item[1] = item[1] - ave
    items = sorted(items,key=lambda x:abs(x[1]))
    pre = None
    cost = 0
    for item in items:
        if item[1] > 0:
            pre = item[0]
            cost= item[1]
        elif item[1] < 0:
            pay = min(cost,abs(item[1]))
            print item[1],pre,pay
            cost -= pay
