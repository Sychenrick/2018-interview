

# N,M,P=map(int,raw_input().split())
# nums = list(map(int,raw_input().split()))
# for i in range(M):
#     command = raw_input().split()
#     index = int(command[1]) - 1
#     if command[0] == 'A':
#         nums[index] += 1
#     else:
#         if nums[index] > 0:
#             nums[index] -= 1
#         else:
#             nums[index] = 0
# pivot = nums[P-1]
# count = 1
# for i in range(N):
#     if  nums[i] > pivot:
#         count += 1
# print count


def compareSort(i, j):
    if i[1] == j[1]:
        return j[1]-i[1]
    else:
        return i[1] - j[1]

def getNums(nums):
    if not nums:
        return 0
    nums.sort(key= lambda x:x[1])
    print nums
    length = len(nums)
    cnt = 1
    end = nums[0][1]
    for i in range(1,length):
        if nums[i][0] < end:
            continue
        cnt += 1
        end = nums[i][1]
    return cnt


N = int(raw_input())
nums = []
for i in range(N):
    temp = list(map(int, raw_input().split()))
    temp.sort()
    nums.append(temp)
res = getNums(nums)
print res