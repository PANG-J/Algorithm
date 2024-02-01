a=int(input())
b=int(input())

print(int(a*(b%10)))
print((a*int((b/10)%10)))
print(int(a*(b//100)))
print(a*b)