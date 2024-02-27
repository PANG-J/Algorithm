R1, S = map(int, input().split()) #첫수 와 평균  
R2 = 0 #R2 0으로 초기화

if R1>0 and S>0 and (R1/2)>=S: #두수가 모두 양수이면서 R1의 평균이 받은 평균보다 클때
    while S != (R1 + R2)/2: #1씩 줄이면서 평균과 맞을 때 찾기
        R2 = R2 - 1
elif R1>0 and S>0: #두수가 모두 양수일때
    while S != (R1 + R2)/2: #1씩 늘리면서 평균과 맞을 때 찾기
        R2 = R2 + 1
elif R1<0 and S<0 and (R1/2)<S: #두수가 모두 음수이면서 R1의 평균이 받은 평균보다 작을때
    while S != (R1 + R2)/2: #1씩 늘리면서 평균과 맞을 때 찾기
        R2 = R2 + 1
elif R1>0 and S<0: #두수가 모두 음수일때
    while S != (R1 + R2)/2: #1씩 줄이면서 평균과 맞을 때 찾기
        R2 = R2 - 1
print(R2)