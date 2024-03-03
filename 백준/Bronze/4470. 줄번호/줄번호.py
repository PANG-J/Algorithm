N = int(input()) #입력받을 문자열 줄의 수

for i in  range(1, N+1): #문자열 줄의 수만큼 반복
    s = input() #문자열 입력받기
    i = str(i) #출력하기 좋도록 숫자를 문자열로 바꾸기
    print(i+". "+s) #+로 연결 해주기
    # print(f"{i}. {s}")