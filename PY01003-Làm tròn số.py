def lam_tron_so(N):
    factor = 10
    while N >= factor:
        N = N - (N % factor) + factor if N % factor >= factor // 2 else N - (N % factor)
        factor *= 10
    return N
if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        print(lam_tron_so(N))