n = int(input())
s = input()

sl = len(s)

for l in range(sl//2, 0, -1):
    start_idx = 0
    while True:
        try:
            search_word = s[start_idx: start_idx+l]
            


    