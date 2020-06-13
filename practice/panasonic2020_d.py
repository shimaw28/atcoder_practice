# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_d

N = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"

curr_str = []

def print_str(curr_str):
    string = ""
    for i in curr_str:
        string += alphabet[i]
    print(string)


def dfs(index, curr_str, curr_char):
    if curr_char > index:
        return None
    if curr_char > max(curr_str) + 1:
        return None

    if index == N-1:
        print_str(curr_str + [curr_char])
        return None

    for i in range(N):
        dfs(index+1, curr_str+[curr_char], i)


if N == 1:
    print("a")
else:    
    for i in range(N):
        dfs(1, [0], i)