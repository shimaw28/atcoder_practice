# p34

n = 4
a = [1,2,4,7]
k = 13

def dfs(i, summ):
    if i == n:
        return summ == k
    
    #a[i]を使わない場合
    if dfs(i+1, summ):
        return True
    
    #a[i]を使う場合
    if dfs(i+1, summ+a[i]):
        return True
    
    return False

if dfs(0,0):
    print("Yes")
else:
    print("No")

