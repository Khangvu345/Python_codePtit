def phan_tich_thua_so(n):
    result = ["1"]
    factor = 2
    while factor * factor <= n:
        count = 0
        while n % factor == 0:
            count += 1
            n //= factor
        if count:
            result.append(f"{factor}^{count}")
        factor += 1
    if n > 1:
        result.append(f"{n}^1")
    return " * ".join(result)

if __name__ == "__main__":
    for _ in range(int(input())):
        print(phan_tich_thua_so(int(input())))