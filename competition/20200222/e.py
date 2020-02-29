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
ans=1
for i in range(1,min(k+1,n)):
  ans=(ans+com(n,i)*hcom(n-i,i)%mod)%mod
print(ans)
