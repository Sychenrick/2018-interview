

def solve(s,t):
    m = len(s)
    n = len(t)
    if m < n:
        return 0
    num = 0
    for i in range(m-n+1):
        substr = s[i:i+n]
        if isOk(substr,t):
            num += 1

    return num
from collections import defaultdict
def isOk(substr,target):
    alpdict1 = defaultdict(int)
    alpdict2 = defaultdict(int)
    for i in range(len(target)):
        sc = substr[i]
        st = target[i]
        if alpdict1[sc] != alpdict2[st]:
            return False
        alpdict1[sc] = i+1
        alpdict2[st] = i+1
    return True



def mapsolve(gird,n,start,visited):
    temp = set()
    per = set()
    visited[start] = 1
    temp.add(start)
    if sum(visited) == n:
        return True

    for i in range(0,n):
        if visited[i]:
            continue

        if grid[start][i]  > 0:
            per.add(i)
        else:
            visited[i] = 1
            temp.add(i)
    if len(per) == 0:
        return True
    for i in per:
        per2 = set(grid[i])
        if not temp.issubset(per2):
            return False

    if mapsolve(grid,n,list(per)[0],visited):
        return True
    else:
        return False


num = int(raw_input())

for _ in range(num):
    n,m = map(int,raw_input().split())
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        temp = list(map(int,raw_input().split()))
        grid[temp[0]-1][temp[1]-1] = temp[1]-1
        grid[temp[1]-1][temp[0]-1] = temp[0]-1
    visited = [0 for _ in range(n)]
    if mapsolve(grid,n,0,visited):
        print "Yes"
    else:
        print "No"


