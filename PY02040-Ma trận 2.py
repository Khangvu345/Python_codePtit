N = int(input())
matrix = []
for _ in range(N):
    rows = list(map(int, input().split()))
    matrix.append(rows)
K = int(input())

sum_top = 0
sum_bottom = 0
for i in range(N):
    for j in range(N):
        if i + j < N - 1:
            sum_top += matrix[i][j]
        elif i + j > N - 1:
            sum_bottom += matrix[i][j]

difference = abs(sum_top - sum_bottom)
print("YES" if difference <= K else "NO")
print(difference)