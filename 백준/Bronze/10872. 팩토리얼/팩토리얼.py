N = int(input()) #정수입력
a = 1 #팩토리얼 값을 저장할 변수선언, 곱셈을 해야하니 1로 설정
for i in range(N):
    a = a * (N-i) #팩토리얼
print(a)