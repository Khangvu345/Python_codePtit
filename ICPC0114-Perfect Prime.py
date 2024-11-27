prime=[1,2,3,5,7]
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def is_perfect_prime(n):
    for i in n:
        if int(i) not in prime:
            return False
    split=list(n)
    m=n[::-1]
    if is_prime(sum([int(i) for i in split])) and is_prime(int(n)) and is_prime(int(m)):
        return True
    return False
for _ in range(int(input())):
    n=input()
    if is_perfect_prime(n):
        print("Yes")
    else:
        print("No")