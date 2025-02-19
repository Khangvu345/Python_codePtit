N, X = map(int, input().split())
primes = []
num = 2

while len(primes) < N:
    if all(num % p != 0 for p in primes):
        primes.append(num)
    num += 1

result = [X]
for p in primes:
    result.append(result[-1] + p)
print(*result)