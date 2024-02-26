N = int(input())

for i in range(N):
    A = 0 #O에 대한 득점수
    B = 0 #점수 총합
    M = list(str(input()))
    for j in range(len(M)):
        if M[j] == "O":
            A = A + 1 #O가 연속되면 득점이 1씩늘어남
            B = B + A #총합에 얻은 득점 더하기
        elif M[j] == "X":
            A = 0  #X가 있으면 늘어난 점수 초기화 
    print(B) #입력 받을때마다 총 점수 출력