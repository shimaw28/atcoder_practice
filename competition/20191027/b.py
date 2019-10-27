N = int(input())

def main():
    if N > 81:
        print("No")
        return None

    for i in range(1, 10):
        if N % i == 0 and N // i <= 9:
            print("Yes")
            return None
    
    print("No")

main()
