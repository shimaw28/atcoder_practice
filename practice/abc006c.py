n, m = map(int, input().split())


flag = False
ans = [0, 0, 0]

def solve(n_people, n_legs, man, senior, baby):
    global ans
    global flag
    if flag == True:
        return True

    if n_people == n:
        if n_legs == m:
            flag = True
            return True
        else:
            return False

    if solve(n_people+1, n_legs+2, man+1, senior, baby) and flag != True:
        ans = [man+1, senior, baby]
        return True
    elif solve(n_people+1, n_legs+3, man, senior+1, baby) and flag != True:
        ans = [man, senior+1, baby]
        return True
    elif solve(n_people+1, n_legs+4, man, senior, baby+1) and flag != True:
        ans = [man, senior, baby+1]
        return True

    
flag = solve(0, 0, 0, 0, 0)

if flag:
    print(ans[0], ans[1], ans[2])
else:
    print("-1 -1 -1")