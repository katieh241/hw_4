def average (l):
    if len(l) == 0:
        return 1
    else:
        return sum(l) // len(l)