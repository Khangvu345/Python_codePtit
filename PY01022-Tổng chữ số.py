def step(s):
    if len(s) == 1:
        return 0
    digit_sum = sum(ord(char) - ord('0') for char in s)
    return 1 + step(str(digit_sum))
n = input().strip()
if len(n) == 1:
    print(1)
else:
    print(step(n))