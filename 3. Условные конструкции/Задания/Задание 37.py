n = int(input())
if 11 <= n % 100 <= 14:
    print('грибов')
elif n % 10 == 1:
    print('гриб')
elif n % 10 >= 2 and n % 10 <= 4:
    print("гриба")
else:
    print('грибов')
