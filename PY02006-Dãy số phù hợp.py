def day_so_phu_hop(a, b):
    for i in range(N):
        if a[i] > b[i]:
            return "NO"
    return "YES"
for _ in range(int(input())):
    N=int(input())
    A=input()
    B=input()
    day_A=[int(i) for i in A.split()]
    day_b=[int(i) for i in B.split()]
    day_A.sort()
    day_b.sort()
    print(day_so_phu_hop(day_A,day_b))
