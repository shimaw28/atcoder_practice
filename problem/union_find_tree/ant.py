# p85 poj1182 食物連鎖

N = 100
K = 7

query = [ #type, x, y
    [1, 101, 1],
    [2, 1, 2],
    [2, 2, 3],
    [2, 3, 3],
    [1, 1, 3],
    [2, 3, 1],
    [1, 5, 5]
]


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


ans = 0

uft = UnionFind(N*3)

for q in query:
    t, x, y = q[0], q[1], q[2]

    if x > N or y > N or x<0 or y<0:
        ans += 1
        continue

    if t == 1:
        if uft.same_check(x, y+N) or uft.same_check(x, y+2*N):
            ans += 1
        else:
            uft.union(x, y)
            uft.union(x+N, y+N)
            uft.union(x+2*N, y+2*N)

    else:
        if uft.same_check(x, y) or uft.same_check(x, y+2*N):
            ans += 1
        else:
            uft.union(x, y+N)
            uft.union(x+N, y+N*2)
            uft.union(x+N*2, y)

print(ans)
