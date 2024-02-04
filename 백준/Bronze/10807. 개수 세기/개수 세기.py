t = int(input())
m = list(map(int, input().split()))
v = int(input())
a=0
for i in range(t):
    if v==m[i]:
        a=a+1
print(a)