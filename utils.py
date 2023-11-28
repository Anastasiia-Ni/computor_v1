def conv_float(num):
    """
    Converts a number to an integer if it's a whole number;
    otherwise, rounds to 4 decimal places.
    """
    return int(num) if float(num).is_integer() else round(num, 4)


def print_error():
    """Prints an error message"""
    print("The formula syntax is incorrect")


def find_gcd(a, b):
    """Finds the greatest common divisor (GCD) of two integers."""
    while b:
        a, b = b, a % b
    return a


def simplify_fraction(numerator, denominator):
    """
    Simplifies a fraction by dividing both numerator and denominator
    by their greatest common divisor (GCD).
    """
    gcd = find_gcd(numerator, denominator)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    return simplified_numerator, simplified_denominator


def irreducible_fraction(numerator, denominator):
    """
    Calculates the irreducible fraction representation
    of the given numerator and denominator.
    Returns:
    - str: The irreducible fraction representation as a string.
           Returns None if the fraction is already irreducible.
    """
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
    """Prints the irreducible fraction representation."""
    print("The irreducible fraction:")
    print(f"X = \033[1m{form}\033[0m.\n")


def print_two_fractions(form1, form2):
    """Prints the irreducible fractions representation."""
    print("The irreducible fraction:")
    if form1:
        print(f"X1 = \033[1m{form1}\033[0m")
    if form2:
        print(f"X2 = \033[1m{form2}\033[0m")
    print()
