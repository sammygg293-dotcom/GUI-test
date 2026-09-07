def is_positive_float(n):
    try:
        if float(n) > 0:
            valid = True
        else:
            valid = False
    except ValueError:
        valid = False
    return valid
