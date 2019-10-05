# Tips
`https://atcoder.jp/contests/abc141/tasks/abc141_d`のように直接問題ページに行くと混まない

# 解法別問題
## heap sort, 優先付けキュー
[2019/9/15　abc141　D](https://atcoder.jp/contests/abc141/tasks/abc141_d)  
[解法](https://atcoder.jp/contests/abc141/submissions/7550044)  

ヒエラルキー型のリストを使って解く
![heap](https://miro.medium.com/max/752/1*Qa4zV-Ys8iXRbPCt2Xt3Zw.png)

`max_heap`,`min_heap`の２種類ある。

[わかりやすい参考](https://medium.com/@yasufumy/data-structure-heap-ecfd0989e5be)

## DFS(Deapth First Search), 深さ優先探索
[abc119 D](https://atcoder.jp/contests/abc119/tasks/abc119_c)
[解法](https://atcoder.jp/contests/abc119/submissions/7567907)

動的プログラミングを使う
p34,　poj2336

[わかりやすい参考](https://pyteyon.hatenablog.com/entry/2019/03/01/211133)

## BSF (Breadth first search)

p36,

## 約数
[abc142 D](https://atcoder.jp/contests/abc142/tasks/abc142_d)
[解法](https://atcoder.jp/contests/abc142/submissions/7769609)

L(N**0.5)
```python
def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table
```

## 素数判定
L(N**0.5)
```python
def is_prime(n):　＃nは素数か判定
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
```

# 実装
## stack
```python 
stack = [3, 4, 5]
#add
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack
[3, 4, 5]
```

## que
```python
>>> from collections import deque
>>> queue = deque(["Erric", "John", "Mary"])
>>> queue.append("Josh")
>>> queue
deque(['Erric', 'John', 'Mary', 'Josh'])
>>> queue.popleft()
'Erric'
>>> queue.popleft()
'John'
>>> queue
deque(['Mary', 'Josh'])
```

