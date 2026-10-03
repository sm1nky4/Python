from math import sqrt


def is_simple(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True



a = int(input())
count = 0
number = 2
while a > count:
    if is_simple(number):
        print(number, end=' ')
        count += 1
    number += 1