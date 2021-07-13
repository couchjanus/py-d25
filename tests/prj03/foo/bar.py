# def plus(args):
#     total = 0
#     for val in args:
#         total += val
#     return total

# def plus(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total

def plus(*args):
    total = 0
    for val in args:
        if type(val) is list:
            total += plus(*val)
        elif type(val) is tuple:
            total += plus(*val)
        else:
            total += val
    return total

