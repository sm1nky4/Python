from math import sqrt


def is_perfect(num):
    div = 1
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            div += i
            div += num // i
    return div == num


n = int(input())
count = 0
a = 2
while count < n:
    if is_perfect(a):
        print(a, end=' ')
        count += 1
    a += 1