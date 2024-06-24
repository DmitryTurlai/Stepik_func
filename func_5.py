def convert(string):
    characters = list(string)
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    if upper_count <= lower_count:
        s = string.lower()
    else:
        s = string.upper()
    return s