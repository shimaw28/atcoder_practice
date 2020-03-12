# https://atcoder.jp/contests/abc145/tasks/abc145_c

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
INF = float("inf")
import itertools

N = INT()
xy = [tuple(MAP()) for _ in range(N)]

dist_list=[]
for i in itertools.permutations(xy, N):
    dist = 0
    for j in range(1, N):
        dist += ((i[j-1][0]-i[j][0])**2 + (i[j-1][1]-i[j][1])**2)**0.5
    dist_list.append(dist)

print(sum(dist_list)/len(dist_list))

