'''
mod付きの組み合わせ
nCk　を求める
nHk　を求める、これはx種類のものから重複を許してy個選ぶ組み合わせ。n個のボールとk-1の仕切りを一列に並べるイメージ
code: https://atcoder.jp/contests/abc156/submissions/10341768
解説:　https://img.atcoder.jp/abc156/editorial.pdf
'''
import sys
input = sys.stdin.readline

N=2*10**5+1
mod=10**9+7
f=[None]*N
fi=[None]*N
f[0]=1
for i in range(1,N):
  f[i]=i*f[i-1]%mod
for i in range(N):
  fi[i]=pow(f[i],mod-2,mod)
def com(n,k):
  return f[n]*fi[n-k]%mod*fi[k]%mod
def hcom(n,k):
  return com(n+k-1,n-1)
n,k=map(int,input().split())



print(comb(n, k) % mod)