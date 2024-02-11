N, M = map(int, input().split())
x = [[0]*M for i in range(N)]
y = [[0]*M for i in range(N)]
for i in range(N):
    x[i] = list(map(int, input().split()))

for i in range(N):
    y[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        x[i][j] = x[i][j] + y[i][j]

for i in range(N):
    for j in range(M):
        print(x[i][j], end=' ')
    print()