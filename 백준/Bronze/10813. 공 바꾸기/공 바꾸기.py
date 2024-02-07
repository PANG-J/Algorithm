N, M = map(int, input().split())
x = []
for a in range(N):
    x.append(a+1)
for a in range(M):
    i, j = map(int, input().split())
    b = x[i-1]
    x[i-1] = x[j-1]
    x[j-1] = b

for a in range(N):
    print(x[a], end=" ")