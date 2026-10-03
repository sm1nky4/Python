def f(n):
    if n > 1:
        f(n//2)
    print(n%2, end='')


n = int(input())
f(n)