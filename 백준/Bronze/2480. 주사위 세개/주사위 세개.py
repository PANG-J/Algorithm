A, B, C = map(int, input().split())

if A==B and B==C and A==C:
    D=10000+(A*1000)
    print(D)
elif B==C or A==C:
    D=1000+(C*100)
    print(D)
elif A==B:
    D=1000+(A*100)
    print(D)
elif A!=B and A!=C and B!=C:
    E=A
    if E<B:
        E=B
    if E<C:
        E=C
    print(E*100)
    