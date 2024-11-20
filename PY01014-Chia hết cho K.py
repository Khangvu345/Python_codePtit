def chia_het_cho_K(a,K,N):
    start_i=K-(a%K)
    if start_i > N-a :
        print(-1)
    else:
        for i in range(start_i,N-a+1,K):
            print(i,end=" ")
a, K, N = map(int, input().split())
chia_het_cho_K(a,K,N)