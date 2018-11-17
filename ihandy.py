
def compare(x,y):
    temp1 = int(x+y)
    temp2 = int(y+x)
    return temp1 < temp2

def getmaxnum(nums):
    if not nums:
        return 0
    nums.sort(cmp=compare,reverse=True)
    temp = ''
    for num in nums:
        temp += num

    return int(temp)

# n = int(raw_input())
# res = []
# for i in range(n):
#     res.append(raw_input())
# num = getmaxnum(res)
# print num

cnt = 0
def fn(n):
    global cnt
    cnt += 1
    if n==0:
        return 0
    if n == 1:
        return 1
    return fn(n-1)+fn(n-2)

fn(5)
print cnt