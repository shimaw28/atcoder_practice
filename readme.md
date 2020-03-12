# Tips

`https://atcoder.jp/contests/abc141/tasks/abc141_d`のように直接問題ページに行くと混まない

# 解法別問題

## 全探索 (full search)

基本`for`文の使い回し  
[link](https://qiita.com/e869120/items/f1c6f98364d1443148b3#1-6-4-%E5%85%A8%E6%8E%A2%E7%B4%A2%E3%81%AB%E6%85%A3%E3%82%8C%E3%82%8B)

### bit全探索  

[bit 全探索](https://drken1215.hatenablog.com/entry/2019/12/14/171657)  

```python
from itertools import product
for i in product([0, 1], repeat=N)
```

や

`1 << N`で2ビットの数字を作るのが便利

## 二分探索(binary_search)

[アルゴリズムを勉強するなら二分探索から始めよう！](https://codezine.jp/article/detail/9900?p=2)

[Python標準ライブラリ：順序維持のbisect](https://qiita.com/ta7uw/items/d6d8f0ddb215c3677cd3)

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
キューとメモを使ってとく

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

# 貪欲法

p42

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

# mod

## modの余剰

[URL](https://img.atcoder.jp/abc156/editorial.pdf)

```python
(X / Y) mod (10**9+7) = X * Y**((10**9+7)-2) mod (10**9+7)

```

## mod付きの組み合わせ

`tutorial/combination/cmb.py`
[URL](https://atcoder.jp/contests/abc156/submissions/10360982)

# bit演算
2bitの数字をフラグが立ってる・立っていないものとして利用する。
[ビット演算 (bit 演算) の使い方を総特集！](https://qiita.com/drken/items/7c6ff2aa4d8fce1c9361)  
[Python ビット演算 超入門](https://qiita.com/7shi/items/41d262ca11ea16d85abc)  


## 例: bitの判定

bit`i`の`k`番目が1であるか:  

```python
if i >> k & 1:
    ...
```

## 例: bitの反転

```std
>>> bin(~1 & 0b1111)
'0b1110'
```

# 参考

https://qiita.com/e869120/items/eb50fdaece12be418faa
