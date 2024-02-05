n = 28
m=[]
x=[]
for i in range(n):
    x.append(int(input()))
for i in range(1, n+3):
    if i not in x:
        m.append(i)
    if len(m) == 2:   
        break
if m[0]>m[1]:
    print(m[1])
    print(m[0])
else:
    print(m[0])
    print(m[1])