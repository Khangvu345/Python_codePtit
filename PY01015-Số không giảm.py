def so_khong_giam(n):
    for i in range(len(n)-1):
        if int(n[i]) > int(n[i+1]):
            return"NO"
    return "YES"
for _ in range(int(input())):
    n=input()
    print(so_khong_giam(n))