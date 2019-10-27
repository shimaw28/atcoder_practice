from collections import deque

N = int(input())
S = input()

new_s = []
flag = True
while flag:

    if len(S) == 1:
        new_s = [1]
        break

    new_s = []
    flag = False
    for i in range(len(S)-1):
        current_char = S[i]

        if current_char == S[i+1]:
            flag = True
            continue
            
        else:
            new_s.append(current_char)

    new_s.append(S[-1])
    S = new_s



print(len(new_s))
