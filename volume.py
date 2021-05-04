def volume (x):
    if type(x) != int:
        return 1
    elif x <=0:
        return 1
    else:
        return x*x*x