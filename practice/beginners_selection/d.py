n = int(input())
a = [int(i) for i in input().split()]

counter = 0
break_flag = False
while True:
    for i in range(len(a)):
        if a[i] % 2 == 1:
            break_flag = True
            break
        else:
            a[i] /= 2
    if break_flag:
        break
    counter += 1

print(counter)


