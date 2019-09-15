b, k = map(int,input().split())
a = list(map(int, input().split()))

#%%
# def main(a, b, k):
#     if b % 2 == 0:
#         return "even"
    
#     if k % 2 == 0:
#         return "even"
    
#     for i in a:
#         if i % 2 == 0:
#             return "even"
    
#     return "odd"

# def main2(a, b, k):
#     ans = 0
#     for i in range(len(a)):
#         ans += a[i] * b ** (k-1-i)
#     if ans % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# print(main2(a, b, k))
def main(a, b, k):
    if b % 2 == 0:
        if a[-1] % 2 != 0:
            return "odd"
        else:
            return "even"

    else:
        ans = 0
        for ai in a:
            if (ans + ai) % 2 == 0:
                ans = 0
            else:
                ans = 1
        
        if ans == 0:
            return("even")
        else:
            return("odd")

print(main(a,b,k))            