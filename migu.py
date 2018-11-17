def  spiralOrder(arr):
    m = len(arr)
    n = len(arr[0])
    r1 = 0
    r2 = m-1
    c1 = 0
    c2 = n-1
    res = []
    while r1 <= r2 and c1 <= c2:
        for i in range(c1,c2+1):
            res.append(arr[r1][i])
        for i in range(r1+1,r2+1):
            res.append(arr[i][c2])
        if r1 != r2:
            for i in range(c2-1,c1-1,-1):
                res.append(arr[r2][i])
        if c1 != c2:
            for i in range(r2-1,r1,-1):
                res.append(arr[i][c1])
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return res

m = int(raw_input())
n = int(raw_input())
raw = list(map(int,raw_input().split()))
arr = [[] for _ in range(m)]
index = 0
for i in range(m):
    j = 0
    while j < n:
        arr[i].append(raw[index])
        j += 1
        index += 1
res = spiralOrder(arr)
for i in res:
    print i