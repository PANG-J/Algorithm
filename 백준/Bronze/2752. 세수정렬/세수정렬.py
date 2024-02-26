X = list(map(int, input().split()))
M = 0

for i in range(len(X)):
    for j in range(i+1, len(X)):
        if X[i] > X[j]:
            M=X[j]
            X[j] = X[i]
            X[i] = M    

for i in range(len(X)):
    print(X[i], end = " ")