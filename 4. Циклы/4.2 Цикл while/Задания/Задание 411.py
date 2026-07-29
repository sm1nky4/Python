b = 0
m2 = 0
while (a:=int(input())) != 0:
    if a > b:
        b = a
        m2 = 1
    elif a == b:
        m2 += 1
print(m2)
