N, M = map(int, input().split())
x=[0 for i in range(N+1)]

for a in range(M):
    i, j, k = map(int, input().split())
    for b in range(i, j+1):
        x[b] = k

for i in range(N):
    print(x[i+1], end=" ")