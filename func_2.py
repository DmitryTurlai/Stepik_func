def same_parity(numbers):
    if numbers:
        chek = numbers[0]
        output = []
        for i in numbers:
            if chek % 2 == i % 2:
                output.append(i)
    else:
        output = []
    return output