N, M = map(int, input().split())

if N<0 and M<0:
    if N>M:
        print(N-M)
    else:
        print(-(N-M))
elif N<0 and M>=0:
    print(-N+M)
elif N>=0 and M<0:
    print(N+(-M))
else:
    if N>M:
        print(N-M)
    else:
        print(M-N)