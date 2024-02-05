n=9
x=[]
for i in range(n):
    x.append(int(input()))
max=x[0]
for i in range(n-1):
    if max<x[i+1]:
        max=x[i+1]
print(max)
for i in range(n):
    if max==x[i]:
        a=i+1
print(a)