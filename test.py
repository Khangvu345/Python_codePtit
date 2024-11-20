def ktnt(n):
    n = int(n)
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


def nguyen_to_dung_vi_tri(x):
    prime_digits = {'2', '3', '5', '7'}
    length = len(x)

    for i in range(length):
        position = i + 1  # Vị trí trong dãy (bắt đầu từ 1)
        digit = x[i]

        if ktnt(position):
            if digit not in prime_digits:
                return 0
        else:
            if digit in prime_digits:
                return 0
    return 1


for _ in range(int(input())):
    y = input()
    if nguyen_to_dung_vi_tri(y):
        print("YES")
    else:
        print("NO")
