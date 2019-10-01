n, m = map(int, input().split())
for i in range(n+1):
  for j in range(min(2, n-i+1)):
    k = n-i-j
    if i*2+j*3+k*4 == m:
      print(i, j, k)
      exit()
print(-1, -1, -1)
