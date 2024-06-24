def print_given(*args, **kwargs):
    for i in range(len(args)):
        print(args[i], type(args[i]))
    for key in sorted(kwargs):
        print(key, kwargs[key], type(kwargs[key]))