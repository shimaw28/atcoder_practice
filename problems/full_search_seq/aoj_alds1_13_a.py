def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

k = INT()
chess = [-1] * 8
R, C = [], []
for _ in range(k):
    r, c = MAP()
    R.append(r); C.append(c)
    chess[r] = c

def check(chess, idx, c):
    for i in range(1, idx+1):
        if chess[idx - i] == c:
            return False
        if chess[idx - i] == c-i:
            return False
        if chess[idx - i] == c+i:
            return False
    return True


def solve(chess, idx):
    if idx == 8:
        return chess
    chess2 = chess.copy()
    

    if chess2[idx] == -1:
        for c in range(8):
            chess2[idx] = c
            if check(chess2, idx, c):
                chess = solve(chess2, idx+1)
    else:
        if check(chess2, idx, chess2[idx]):
            chess = solve(chess2, idx+1)
    return chess

print(solve(chess, 0))


