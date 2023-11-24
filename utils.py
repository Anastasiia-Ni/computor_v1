def conv_float(num):
    return int(num) if float(num).is_integer() else round(num, 4)


def print_error():
    print("The formula is not correct")