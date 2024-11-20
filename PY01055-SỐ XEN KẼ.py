def so_xen_ke(n):
    ds=list(n)
    dk3=set()
    for i in range(0,len(ds),2):
        dk3.add(ds[i])
    if len(dk3)==1 and len(ds) % 2 == 1 and n[0] != n[1]:
        print("YES")
        return
    print("NO")
for _ in range(int(input())):
    m=input()
    so_xen_ke(m)