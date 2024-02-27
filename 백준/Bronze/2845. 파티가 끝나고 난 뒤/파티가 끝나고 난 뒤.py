L, P = map(int, input().split())
X = list(map(int, input().split()))

for i in range(len(X)):
    X[i] = X[i] - (L*P)
for i in range(len(X)):
    print(X[i], end = " ")   