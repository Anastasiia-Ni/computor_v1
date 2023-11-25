def conv_float(num):
    return int(num) if float(num).is_integer() else round(num, 4)


def print_error():
    print("The formula is not correct")


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    gcd = find_gcd(numerator, denominator)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    return simplified_numerator, simplified_denominator


def irreducible_fraction(numerator, denominator):
    if float(numerator).is_integer():
        numerator = int(numerator)
    if float(denominator).is_integer():
        denominator = int(denominator)

    if isinstance(numerator, int) and isinstance(denominator, int):
        numerator, denominator = simplify_fraction(numerator, denominator)

    if find_gcd(numerator, denominator) == 1 and denominator != 1:
        if numerator < 0 and denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
        elif denominator < 0:
            numerator = -numerator
            denominator = abs(denominator)
        return f"{numerator} / {denominator}"
        
    return None 
        

def print_one_fraction(form):
    print("The irreducible fraction:")
    print(f"X = \033[1m{form}\033[0m.\n")


def print_two_fraction(form1, form2):
    print("The irreducible fraction:")
    if form1:
        print(f"X1 = \033[1m{form1}\033[0m")
    if form2:
        print(f"X2 = \033[1m{form2}\033[0m")
    print()

