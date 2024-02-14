r = ""
for i in input(): #받은 문자열을 바로 순회
    if i.isupper(): #문자가 대문자인지 확인하는 코드
        r = r + i.lower() #문자를 소문자로 변경하는 코드
    else:
        r = r + i.upper() #문자를 대문자로 변경
print(r)