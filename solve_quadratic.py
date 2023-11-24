from utils import conv_float

def solve_discriminant2(formula):
    print(f"Calculate the discriminant:")
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
    print(f"Δ = {conv_float(d)}")

    return d

def discriminant2_zero(formula, d):
    print('The solution is:')
    b = formula["x1"]
    a = formula["x2"]
    print(f"X = -({conv_float(b)}) / (2 * ({conv_float(a)}))")
    print(f"X = -({conv_float(b)}) / ({conv_float(2 * a)})")
    x = b / (2 * a)
    print(f"X = {conv_float(x)}")


def discriminant2_positive(formula, d):
    print('The solutions are:')
    b = formula["x1"]
    a = formula["x2"]

    print(f"X = (-({conv_float(b)}) ± √{conv_float(d)}) / (2 * ({conv_float(a)}))")

    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)

    sign = '+' if b < 0 else '-'
    b2 = abs(b)
    print(f"X = ({sign}{b2} ± {conv_float(d ** 0.5)}) / ({conv_float(2 * a)})")

    print(f"X1 = ({conv_float(-b + (d ** 0.5))}) / ({conv_float(2 * a)})")
    print(f"X2 = ({conv_float(-b - (d ** 0.5))}) / ({conv_float(2 * a)})")

    print(f"X1 = {conv_float(x1)}")
    print(f"X2 = {conv_float(x2)}")


def discriminant2_negative(formula, d):
    print('The solutions are:')
    b = formula["x1"]
    a = formula["x2"]

    print(f"X = (-({conv_float(b)}) ± √{conv_float(d)}) / (2 * ({conv_float(a)}))")

    d = abs(d)
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)

    sign = '+' if b < 0 else '-'
    b2 = abs(b)
    print(f"X = ({sign}{b2} ± {conv_float(d ** 0.5)}√-1) / ({conv_float(2 * a)})")
    print("Let √-1 = i imaginary unit, then")
    print(f"X1 = ({conv_float(-b + (d ** 0.5))}i) / ({conv_float(2 * a)})")
    print(f"X2 = ({conv_float(-b - (d ** 0.5))}i) / ({conv_float(2 * a)})")

    print(f"X1 = {conv_float(x1)}i")
    print(f"X2 = {conv_float(x2)}i")


def solve_quadratic_equation(formula):
    d = solve_discriminant2(formula)
    if d == 0:
        print("Discriminant is zero, the equation has one real solution.")
        discriminant2_zero(formula, d)
    elif d > 0:
        print("Discriminant is strictly positive, the equation has two solutions.")
        discriminant2_positive(formula, d)
    else:
        print("Discriminant is strictly negative, the equation has two complex solutions.")
        discriminant2_negative(formula, d)