T = int(input())

for i in range(T):
    R, S = map(list, input().split())
    for i in range(len(S)):
        S[i] = S[i] * int(R[0])
    for i in range(len(S)):
        print(S[i], end='')
    print()
    for i in range(len(S)):
        S[i] = ''
