def kiem_tra_so_dep(n):
    nhom_chu_so=set(n)
    chu_so_vi_tri_chan=str(n)[0::2]
    chu_so_vi_tri_le=str(n)[1::2]
    if len(nhom_chu_so)==2 and len(set(chu_so_vi_tri_chan))==len(set(chu_so_vi_tri_le))==1:
        return "YES"
    return "NO"
for _ in range(int(input())):
    n=input()
    print(kiem_tra_so_dep(n))
