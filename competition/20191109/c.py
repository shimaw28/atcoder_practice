import numpy as np

N = int(input())
A = np.array([int(i) for i in input().split()])
B = np.array([int(i) for i in input().split()])

def main():
    if A.sum() > B.sum():
        print("No")
        return None

    isAGreater = A > B
    if isAGreater.sum() > N-2:
        print("No")
        return None
    
    

main()