def main():
    import sys
    input = sys.stdin.readline
 
    mod = 1000000007
    nmax = 2 * 10 ** 5 + 10  # change here
    fac = [0] * nmax
    finv = [0] * nmax
    inv = [0] * nmax
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, nmax):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
 
    def comb(n, r):
        ret = finv[r]
        for i in range(r):
            ret = (ret * (n-i))%mod
        return ret
    N, a, b = map(int, input().split())
    print((pow(2, N, mod) - 1 - comb(N, a) - comb(N, b))%mod)
 
 
if __name__ == '__main__':
    main()