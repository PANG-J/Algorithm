M = 0
S = 0
for i in range(4):
    N = int(input()) #초를 입력 받기
    S = N + S #남은 초를 입력받은 초와 더해주기
    while S>59: #더한 초를 다시 분으로 환산, 60초가 넘으면 1분더해주기
        S = S - 60
        M = M + 1
print(M) #분 출력
print(S) #초 출력