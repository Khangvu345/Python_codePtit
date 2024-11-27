x=input()
y=len(x)
pick=[0]*y
def permutation(a,b):
    if b==y:
        print(a)
        return
    for i in range(y):
        if pick[i]==0:
            pick[i]=1
            permutation(a+x[i],b+1)
            pick[i]=0
permutation("",0)