
klist = [str(i) for i in range(10)] + ['a','b','c','d','e','f']

def mostLong(start,end,k):
    if start > end:
        return 0
    minnum = numLength(start,k)
    maxnum= numLength(end,k)
    maxlen = len(maxnum)
    minlen = len(minnum)
    minnum = '0'*(maxlen-minlen)+minnum
    index = klist[k-1]
    for i in range(maxlen):
        pass




def numLength(num,k):
    cnt = []
    while num > 0:
        cnt.append(klist[num % k])
        num /= k
    cnt.reverse()
    return ''.join(cnt)


q = int(raw_input())
for i in range(q):
    k, start, end = map(int,raw_input().split())
    print mostLong(start,end,k)
