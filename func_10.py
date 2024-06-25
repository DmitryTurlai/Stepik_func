def choose_plural(amount, declensions):
    marker = 0
    a = amount
    while amount > 20:
        if amount > 100:
            amount %= 100
        elif amount > 20:
            amount %= 10
    if amount == 0:
        marker = 2
    elif amount == 1:
        marker = 0
    elif 1 < amount < 5:
        marker = 1
    elif 4 < amount < 20:
        marker = 2
    res = f'{a} {declensions[marker]}'
    return res

print(choose_plural(240, ('курица', 'курицы', 'куриц')))