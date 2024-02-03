t = int(input())
c=0
for i in range(1, t+1):
    A, B = map(int, input().split())
    print("Case #"+str(i)+":", A+B)