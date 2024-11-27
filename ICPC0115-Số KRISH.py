from math import*
for _ in range(int(input())):
    n=input()
    sum_factorial=0
    for i in n:
        sum_factorial+=factorial(int(i))
    print("YES" if sum_factorial==int(n) else "NO")
