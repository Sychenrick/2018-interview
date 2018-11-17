def cntNum(nums):
    global cnt
    if len(nums) == 1:
        return 1
    pre = 0
    index = 0
    for i in range(1,len(nums)):
        if nums[i] - nums[i-1] > pre:
            pre = nums[i] - nums[i-1]
            index = i-1
    if pre == 0:
        return
    nums[index+1] = nums[index]
    cnt += 1
    cntNum(nums)


# n = int(raw_input())
# for i in range(n):
#     m = int(raw_input())
#     nums = list(map(int,raw_input().split()))
#     allsum = sum(nums)
#     cnt = m
#     cnt += len(nums)
#     print cnt
#     if cnt % 2 == 0:
#         print "Moon"
#     else:
#         print "Star"
def merge(nums,l,mid,r,temp):
    i = l
    j = mid+1
    for t  in range(l,r+1):
        temp[t] = nums[t]
    for k in range(l,r+1):
        if i > mid:
            nums[k] = temp[j]
            j += 1
        elif j > r:
            nums[k] = temp[i]
            i += 1
        elif temp[i] <= temp[j]:
            nums[k] = temp[i]
            i += 1
        else:
            nums[k] = temp[j]
            j += 1


def mergeSort(nums,i,j,temp):
    if i >= j:
        return
    mid = i + (j-i)/2
    mergeSort(nums,i,mid,temp)
    mergeSort(nums,mid+1,j,temp)
    merge(nums,i,mid,j,temp)
def merge_sort(nums):
    temp = [None for _ in nums]
    mergeSort(nums,0,len(nums)-1,temp)

def quickSort(nums,l,r):
    if l >= r:
        return
    i = l
    j = r
    pivot = nums[i]
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pivot:
            i += 1
        nums[j] = nums[i]
    nums[i] = pivot
    quickSort(nums,0,i-1)
    quickSort(nums,i+1,r)

def quick_sort(nums):
    quickSort(nums,0,len(nums)-1)


def rawinput(strlist):
    temp = ''
    for i in range(0,10):
        temp += str(i)


