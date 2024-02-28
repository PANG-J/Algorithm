S, M = map(int, input().split()) #점수의 합과 차를 받는다
#A+B=S, A-B=M, 결국 2B = S + M
if (S+M)%2 != 0 or S<M: 
    #차가 합보다 크면 성립이 되지않고, 합과 차의 합이 짝수가 되지 않으면 성립되지 않는다.
    print(-1)
elif S>=M: #합이 차보다 커야 식이 성립이 된다
    B = (S+M)//2 #이렇게 안해주고 /만 해주면 float형식으로 바뀐다
    print(B, S-B) #A+B=S, S-B=A, 무조건 B가 더 크기 때문에 B, S-B