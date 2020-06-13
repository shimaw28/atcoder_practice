# https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, A, B = MAP()
S = input()

passed = 0
b_cnt = 1
for s in S:
    if s == "a":
        if passed < A + B:
            passed += 1
            print("Yes")
        else:
            print("No")
    elif s == "b":
        if passed < A + B and b_cnt <= B:
            print("Yes")
            passed += 1
        else:
            print("No")
        b_cnt += 1
    else:
        print("No")