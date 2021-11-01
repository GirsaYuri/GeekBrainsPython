for i in range(1, 101):
    if i >= 0:
        if i == 1:
            print(f'{i} процент')
        elif i % 100 >= 10 and i % 100 <= 20:
            print(f'{i} процентов')
        elif i % 10 == 1:
            print(f'{i} процент')
        elif i % 10 >= 2 and i % 10 <= 4:
            print(f'{i} процента')
        else:
            print(f'{i} процентов')
