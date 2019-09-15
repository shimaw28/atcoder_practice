import pandas as pd

n, m = map(int, input().split())

p = []
y = []

for i in range(n):
    pi, yi = map(int, input().split):
    p.append(pi)
    y.append(yi)


df = pd.DataFrame({"p": p, "y": y})

df["ranked"] = df.groupby("p").rank()

for i in range(n):
    print(str(df.iloc[0].p.astype(int)).zfill(6) + str(df.iloc[0].ranked.astype(int)).zfill(6))
