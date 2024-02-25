while 1:
    Name, A, B = map(str, input().split())
    if Name == '#':
        break
    if int(A)>17 or int(B)>=80:
        print(Name, "Senior")
    else:
        print(Name, "Junior")