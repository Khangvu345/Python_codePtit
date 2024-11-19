for _ in range(int(input())):
    x=input()
    giai_ma=""
    ky_tu=""
    for i in x:
        if i.isalpha():
            ky_tu+=i
        elif i.isdigit():
            dem=int(i)
            while dem>0:
                giai_ma+=ky_tu
                dem-=1
            ky_tu=""
    print(giai_ma)