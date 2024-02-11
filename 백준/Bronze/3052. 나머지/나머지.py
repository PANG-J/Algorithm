x = [0]*10
for i in range(10):
    x[i] = int(input())%42

# 서로 다른 나머지의 개수를 저장할 변수 초기화
a = 0
# 이미 계산된 나머지를 체크하기 위한 리스트
n = []
for i in x:
    # 현재 나머지가 calculated_remainders 리스트에 없다면
    if i not in n:
        # 나머지를 리스트에 추가
        n.append(i)
        # 서로 다른 나머지의 개수를 증가
        a += 1
print(a)