i = 0
while 1:
    x = input()
    if x == "#": #마지막에는 #으로 마무리 지으니 #
        break
    x = x.lower()
    i = x.count('a') + x.count('e') + x.count('i') + x.count('o') + x.count('u')
    print(i)