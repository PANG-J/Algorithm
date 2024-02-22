T, S = map(int, input().split())

if 12>T or T>16 or S==1:
    print(280)
elif 12<=T<=16 or S==0:
    print(320)