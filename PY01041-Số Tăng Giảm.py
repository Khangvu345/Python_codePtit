def so_tang_giam(n):
    if len(n) < 3 :
        return "NO"
    for i in range(1,len(n)-1):
        left=True
        for j in range(0,i):
            if n[j] >= n[j+1]:
                left=False
                break
        right=True
        for j in range(i,len(n)-1):
            if n[j] <= n[j+1]:
                right=False
                break
        if left and right:
            return "YES"
    return "NO"
for _ in range(int(input())):
    n=input().strip()
    print(so_tang_giam(n))