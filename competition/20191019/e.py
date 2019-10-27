N, M, L = map(int, input().split())
abc = []
for _ in range(M):
    abc.append(input().split())
Q = int(input())
st = []
for _ in range(Q):
    st.append(input().split())

print(N, M, L)
print(abc)
print(Q)
print(st)