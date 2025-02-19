N = int(input())
arr = []

while len(arr) < N:
    arr.extend(map(int, input().split()))

M = arr[-1]
missing = []

for i in range(1, M + 1):
    if i not in arr:
        missing.append(i)
if len(missing) > 0:
    for m in missing:
        print(m)
else:
    print("Excellent!")
