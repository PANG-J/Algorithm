A, B, C = map(int, input().split()) #공백으로 나눠서 들어오는 시, 분, 초 입력받기
D = int(input()) #초 입력받기

B = B + (D//60) #D를 60초로 나누어 분에 더해주기
C = C + (D%60) #분에 더해준 나머지 초를 입력받은 초에 더해주기

while C>59: #초가 60이 넘어가면 계속 분에 1을 더해주고 남은 초를 보고 다시 반복
    C=C-60
    B=B+1

while B>59: #분이 60이 넘어가면 시간에 1을 더해주고 남은 초를 보고 다시 반복ㅔ
    B=B-60
    A=A+1

while A>23: 
    A=A-24

print(A, B, C) #공백으로 출력