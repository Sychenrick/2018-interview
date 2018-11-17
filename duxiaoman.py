
import sys
from collections import defaultdict


def get_result(point_weights):

    edge_weights = [0 for i in range(len(point_weights) - 1)]

    left_map = defaultdict(int)
    right_map = defaultdict(int)

    for w in point_weights:
        right_map[w] += 1

    w_i = point_weights[0]
    left_map[w_i] += 1
    right_map[w_i] -= 1
    edge_weights[0] = len(point_weights) - 1 - right_map.get(w_i)

    for i in range(1, len(edge_weights)):
        w_i = point_weights[i]
        left_leave, right_leave = i, len(point_weights) - i
        if left_map.get(w_i, 0) > 0:
            edge_weights[i] = edge_weights[i - 1] - (left_leave - left_map.get(w_i, 0))
            edge_weights[i] += (right_leave - right_map.get(w_i, 0))
        else:
            edge_weights[i] = edge_weights[i - 1] - left_leave
            edge_weights[i] += (right_leave - right_map.get(w_i, 0))

        left_map[w_i] += 1
        left_leave += 1
        right_map[w_i] -= 1
        right_leave -= 1

    return edge_weights


if __name__ == "__main__":
    while True:
        try:
            n = int(sys.stdin.readline().strip())
        except Exception as e:
            break

        point_weights = list(map(int, sys.stdin.readline().strip().split()))
        print(" ".join(map(str, get_result(point_weights))))



# n = int(raw_input())
# nums = list(map(int,raw_input().split()))
#
# res = calW(nums)
# print ' '.join([str(i) for i in res])


# def whichwin(a,b,n,cnt):
#     if a**b >= n:
#         return cnt
#     if (a+1)**b > a**(b+1):
#         return whichwin(a,b+1,n,cnt+1)
#     else:
#         return whichwin(a+1,b,n,cnt+1)
#
# num = int(raw_input())
# for i in range(num):
#     cnt = 0
#     a,b,n = map(int,raw_input().split())
#     if a == 1:
#         print "A&B"
#         continue
#     else:
#         res = whichwin(a,b,n,cnt)
#         if res % 2 == 0:
#             print "B"
#         else:
#             print "A"


