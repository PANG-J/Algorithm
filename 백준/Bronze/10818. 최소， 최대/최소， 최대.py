n = int(input())
t = list(map(int, input().split()))
min = t[0]
max = t[0]
for i in range(n-1):
    if max<t[i+1]:
        max = t[i+1]
    if min>t[i+1]:
        min = t[i+1]
print(min, max)