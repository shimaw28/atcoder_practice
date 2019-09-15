a, b, c, x = [int(input()) for _ in range(4)]
x //= 50

counter = 0
for i in range(a+1):
    if 10*i > x:
        break
    rem = x - 10* i

    for j in range(b+1):
        if 2*j > rem:
            break
        if rem - 2*j <= c:
            counter += 1

print(counter)            
