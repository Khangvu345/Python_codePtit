def ktnt(n):
    n=int(n)
    if n<2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
def nguyen_to_dung_vi_tri(x):
   for i in range(len(x)):
       if ktnt(i) and not ktnt(x[i]):
           return 0
       elif not ktnt(i) and ktnt(x[i]):
            return 0
   return 1
for _ in range(int(input())):
    y=input()
    if nguyen_to_dung_vi_tri(y):
        print("YES")
    else:
        print("NO")