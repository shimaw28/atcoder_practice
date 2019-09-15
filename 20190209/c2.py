k, a, b = map(int, input().split())

def main(k, a, b):
    if k + 1 < a + 1:
        return k + 1

    dif = b - a
    


    if b > a + 2:
        if k + 1 == a + 2:
            return b + (k-a+1)//(a + 2) * b + (k-a+1) % (a + 2)
        else:
            return k//(a + 2) * b + k % (a + 2) + 1
    
    else:
        return k + 1


print(main(k, a, b))        
