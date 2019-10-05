n, k = map(int, input().split())

#%%

def main():
    if n % 2 == 0:
        if n//2 >= k:
            return "YES"
    else:
        if n//2 + 1 >= k:
            return "YES"

    return "NO"

print(main())    