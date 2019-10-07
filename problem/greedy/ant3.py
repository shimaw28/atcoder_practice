
# p45 dictionary 
# poj3617

n = 6
s = "acdbcb"


t = ""
while len(s) > 1:
    s_ = s[::-1]
    if s[0] < s_[0]:
        t += s[0]
        s = s[1:]
    else:
        t += s_[0]
        s = s[:-1]

t += s
print(t)
