N = int(input())
S = []
words ={}
for _ in range(N):
    si = input()
    if si not in words.keys():
        words[si] = 1
    else:
        words[si] += 1

words_sorted = sorted(words.items(), key=lambda x: x[0])
words_sorted = sorted(words_sorted, key=lambda x: x[1], reverse=True)

max_n = words_sorted[0][1]

for w in words_sorted:
    if w[1] == max_n:
        print(w[0])
    else:
        break
