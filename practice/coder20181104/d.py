# h, w, k = 3, 4, 1


import pandas as pd
import numpy as np

h, w, k = map(int, input().split())

def amida(a, h, w):
    position = 0
    for y in range(h):
        # print(position)
        # print(y)
        if (a[y, position]) and (position != w-1):
            # print("right")
            position += 1
        elif (a[y, position - 1]) and (position != 0):
            # print("left")
            position -= 1

    return position


def check_amida(a, h, w):
    for y in range(h):
        for x in range(w-2):
            if a[y, x]==1 and a[y, x+1]==1:
                return False

    return True


counter = 0
for i in range(2**(h * (w-1))):
    a = np.array(list("{0:b}".format(i).zfill(h*(w-1)))).reshape(h, w-1).astype(bool)
    if check_amida(a, h, w):
        if amida(a, h, w) == k:
            counter += 1

print(counter)
