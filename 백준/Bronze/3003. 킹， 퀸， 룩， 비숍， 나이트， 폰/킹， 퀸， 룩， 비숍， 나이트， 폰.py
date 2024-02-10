n = list(map(int, input().split()))

for i in range(len(n)):
    a=0 
    if i == 0:
        if n[i] == 1:
            n[i] = 0
        elif n[i] > 1:
            while n[i] > 1:
                n[i] = n[i] - 1
                a = a - 1
            n[i] = a
        elif n[i] < 1:
            while n[i] < 1:
                n[i] = n[i] + 1
                a = a + 1
            n[i] = a
    elif i == 1:
        if n[i] == 1:
            n[i] = 0
        elif n[i] > 1:
            while n[i] > 1:
                n[i] = n[i] - 1
                a = a - 1
            n[i] = a
        elif n[i] < 1:
            while n[i] < 1:
                n[i] = n[i] + 1
                a = a + 1
            n[i] = a
    elif i == 2 or i == 3 or i == 4:
        if n[i] == 2:
            n[i] = 0
        elif n[i] > 2:
            while n[i] > 2:
                n[i] = n[i] - 1
                a = a - 1
            n[i] = a
        elif n[i] < 2:
            while n[i] < 2:
                n[i] = n[i] + 1
                a = a + 1
            n[i] = a
    elif i == 5:
        if n[i] == 8:
            n[i] = 0
        elif n[i] > 8:
            while n[i] > 8:
                n[i] = n[i] - 1
                a = a - 1
            n[i] = a
        elif n[i] < 8:
            while n[i] < 8:
                n[i] = n[i] + 1
                a = a + 1
            n[i] = a

for i in range(len(n)):
    print(n[i], end=' ')