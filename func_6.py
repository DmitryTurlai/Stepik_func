def filter_anagrams(word, words):
    res = []
    rs = False
    for w in words:
        if len(w) == len(word) and sorted(w) == sorted(word):
            rs = True
        else:
            rs = False
        if rs == True:
            res.append(w)
    return res
