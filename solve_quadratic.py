from utils import conv_float, irreducible_fraction, \
    print_one_fraction, print_two_fractions


def solve_discriminant2(formula):
    """Calculates and prints the discriminant for a quadratic equation."""
    print("\033[35mCalculate the \033[1mdiscriminant:\033[0m")
    a = conv_float(formula["x2"])
    b = conv_float(formula["x1"])
    c = conv_float(formula["x0"])
    print(f"Δ = ({b})^2 - 4 * ({a}) * ({c})")

    d1 = formula["x1"] ** 2
    d2 = 4 * formula["x2"] * formula["x0"]
    d = d1 - d2
    sign = '+' if d2 < 0 else '-'
    d2 = abs(d2)
    print(f"Δ = {conv_float(d1)} {sign} {conv_float(d2)}")
    print(f"Δ = \033[1m{conv_float(d)}\033[0m\n")
    return d


def discriminant2_zero(formula):
    """Calculates and prints the solution when the discriminant is zero."""
    b = formula["x1"]
    a = formula["x2"]
    print(f"X = -({conv_float(b)}) / (2 * ({conv_float(a)}))")
    print(f"X = -({conv_float(b)}) / ({conv_float(2 * a)})\n")
    x = -b / (2 * a)
    print("\033[35mThe solution is:\033[0m")
    print(f"X = \033[35m\033[1m{conv_float(x)}\033[0m\n")

    if ir_fract := irreducible_fraction(-b, 2 * a):
        print_one_fraction(ir_fract)


def discriminant2_positive(formula, d):
    """Calculates and prints the solution when the discriminant is positive."""
    b = formula["x1"]
    a = formula["x2"]

    print(f"X = (-({conv_float(b)}) ± √{conv_float(d)}) / "
          f"(2 * ({conv_float(a)}))")

    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)

    sign = '+' if b < 0 else '-'
    b2 = abs(b)
    print(f"X = ({sign}{b2} ± {conv_float(d ** 0.5)}) / ({conv_float(2 * a)})")

    print(f"X1 = ({conv_float(-b + (d ** 0.5))}) / ({conv_float(2 * a)})")
    print(f"X2 = ({conv_float(-b - (d ** 0.5))}) / ({conv_float(2 * a)})\n")

    print("\033[35mThe solutions are:\033[0m")
    print(f"X1 = \033[35m\033[1m{conv_float(x1)}\033[0m")
    print(f"X2 = \033[35m\033[1m{conv_float(x2)}\033[0m\n")

    ir_fract1 = irreducible_fraction(-b + (d ** 0.5), 2 * a)
    ir_fract2 = irreducible_fraction(-b - (d ** 0.5), 2 * a)

    if ir_fract1 or ir_fract2:
        print_two_fractions(ir_fract1, ir_fract2)


def discriminant2_negative(formula, d):
    """Calculates and prints the solution when the discriminant is negative."""
    b = formula["x1"]
    a = formula["x2"]

    print(f"X = (-({conv_float(b)}) ± √{conv_float(d)}) / "
          f"(2 * ({conv_float(a)}))")

    d = abs(d)
    x1 = -b / (2 * a)
    x2 = (d ** 0.5) / (2 * a)

    sign = '' if b < 0 else '-'
    b2 = abs(b)
    print(f"X = ({sign}{b2} ± {conv_float(d ** 0.5)}√-1) / "
          f"({conv_float(2 * a)})")
    print("Let √-1 = i imaginary unit, then")
    print(f"X = {conv_float(-b)} / {conv_float(2 * a)} ± "
          f"{conv_float(d ** 0.5)}i / {conv_float(2 * a)}")
    x2 = abs(x2)
    print("\n\033[35mThe solutions are:\033[0m")
    print(f"X1 = \033[35m\033[1m{conv_float(x1)} - {conv_float(x2)}i\033[0m")
    print(f"X2 = \033[35m\033[1m{conv_float(x1)} + {conv_float(x2)}i\033[0m\n")


def solve_quadratic_equation(formula):
    """Take the discriminant and determine the method for further solution."""
    d = solve_discriminant2(formula)
    if d == 0:
        print("\033[35mDiscriminant is zero, the equation has "
              "one real solution.\033[0m")
        discriminant2_zero(formula)
    elif d > 0:
        print("\033[35mDiscriminant is strictly positive, "
              "the equation has two solutions.\033[0m")
        discriminant2_positive(formula, d)
    else:
        print("\033[35mDiscriminant is strictly negative, "
              "the equation has two complex solutions.\033[0m")
        discriminant2_negative(formula, d)
