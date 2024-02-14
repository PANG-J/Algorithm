N = list(map(int, input().split()))
a = 0
for i in range(len(N)):
    a = a + N[i]**2
print(a%10)