def index_of_nearest(numbers, number):
    base = []
    if numbers == []:
        res = -1
    else:
        for n in numbers:
            base.append(abs(number - n))

        min_value = min(base)
        min_index = base.index(min_value)
        res = min_index

    return res