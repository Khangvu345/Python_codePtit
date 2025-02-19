for _ in range(int(input())):
    N = int(input())
    arr = []
    if N % 2 == 0:
        for i in range(2,N+1,2):
           arr.append(1/i)
    else:
        for i in range(1,N+1,2):
            arr.append(1/i)
    result = sum(arr)
    print(f"{result:.6f}")