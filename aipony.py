

def resotre(nums):
    for i in range(1,len(nums)-1):
        while nums[i] <= nums[i-1] and nums[i] <= nums[i+1]:
            nums[i] *= 2
    sub = nums[1] - nums[0]
    nums[-1] = nums[-2]+sub
    return nums

N = int(raw_input())
nums = []
for i in range(N):
    nums.append(int(raw_input()))
nums = resotre(nums)
for i in nums:
    print i


# black = 0
# white = 0
# graph = []
# for i in range(15):
#     rawlist = list(raw_input())
#     graph.append(rawlist)
#
# if abs(black-white) > 1:
#     print "invalid board"
#
# direction = [[0,1],[0,-1],[1,0],[-1,0],
#        [-1,-1],[1,1],[1,-1],[-1,1]]
# def dfs(graph,i,j,std,cnt):
#     if i < 0 or j < 0 or i >= 15 or j >= 15 or graph[i][j] != std:
#         return cnt >= 5
#     temp = graph[i][j]
#     graph[i][j] = '.'
#     cnt += 1
#     for d in direction:
#         if dfs(graph,i+d[0],j+d[1],std,cnt):
#             return True
#         cnt -= 1
#         graph[i][j] = temp
#
#
# def judge(grahp):
#     cnt1 = 0
#     cnt2 = 0
#     for i in range(15):
#         for j in range(15):
#             if graph[i][j] != '.':
#                 if dfs(graph,i,j,'B',cnt1):
#                     return "black win"
#                 elif dfs(graph,i,j,'W',cnt2):
#                     return "white win"
#     if black+white == 225:
#         return "draw"
#     return "not finished"
#
# print judge(graph)







