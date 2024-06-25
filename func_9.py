def spell(*args):
    res = {}
    for i in range(len(args)):
        if args[i][0].lower() in res and res[args[i][0].lower()] < len(args[i]) or args[i][0].lower() not in res:
            res[args[i][0].lower()] = len(args[i])
    return res