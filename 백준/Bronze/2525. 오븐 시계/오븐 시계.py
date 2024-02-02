A, B=map(int, input().split())
C=int(input())

B=B+C
while B>59:
    A=A+1
    B=B-60
    
if A>23:
    A=A-24
print(A, B)