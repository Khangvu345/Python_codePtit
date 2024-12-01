def test_ip(n):
    if len(n) != 4:
        return 0
    for i in n:
        if not i.isdigit():
            return 0
        elif int(i) < 0 or int(i) > 255 :
            return 0
    return 1
for _ in range(int(input())):
    x=input()
    m=[i for i in x.split(".")]
    if test_ip(m):
        print("YES")
    else:
        print("NO")
