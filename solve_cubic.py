from utils import conv_float


def solve_cubic_equation(formula):
    """Take the discriminant and determine method for further solution."""

    p, q = find_coefficients(formula)
    discriminant = solve_discriminant3(p, q)

    if discriminant > 0:
        print("\033[35mThe discriminant is positive, the equation has "
              "one real and two complex solutions.\033[0m")
        discriminant3_positive(formula, discriminant, q)
    elif discriminant == 0:
        print("\033[35mDiscriminant is zero, all three roots are real, "
              "two or three of them are the same.\033[0m")
        discriminant3_zero(formula, q)
    else:
        print("\033[35mThe discriminant is negative, the equation has "
              "three real solutions.\033[0m")
        discriminant3_negative(formula, discriminant, q)


def find_coefficients(formula):
    """Finds the coefficients used in solving the discriminant."""

    a = formula["x3"]
    b = formula["x2"]
    c = formula["x1"]
    d = formula["x0"]

    print("\033[35mCoefficients for calculating the discriminant:\033[0m")

    print("Cubic Viète Coefficients:")
    p = (3 * a * c - b * b) / (3 * a * a)
    print(f"\033[3mp\033[0m = (3 * ({conv_float(a)}) * ({conv_float(c)}) - "
          f"({conv_float(b)})^2) / (3 * ({conv_float(a)})^2)")
    print(f"\033[3mp\033[0m = \033[1m{conv_float(p)}\033[0m")

    q = (2 * b * b * b - 9 * a * b * c + 27 * a * a * d) / (27 * a * a * a)
    print(f"\033[3mq\033[0m = (2 * ({conv_float(b)})^3 - 9 * "
          f"({conv_float(a)}) * ({conv_float(b)}) * ({conv_float(c)}) + "
          f"27 * ({conv_float(a)})^2 * ({conv_float(d)})) / "
          f"(27 * ({conv_float(a)})^3)")
    print(f"\033[3mq\033[0m = \033[1m{conv_float(q)}\033[0m\n")
    return p, q


def solve_discriminant3(p, q):
    """Calculates and prints the discriminant for a cubic equation."""

    print("\033[35mCalculate the \033[1mdiscriminant:\033[0m")

    print(f"Δ = ({conv_float(q)})^2 / 4 + ({conv_float(p)})^3 / 27")
    discriminant = q * q / 4 + p * p * p / 27
    d1 = q * q / 4
    d2 = p * p * p / 27
    sign = '+' if d2 >= 0 else '-'
    d2 = abs(d2)
    print(f"Δ = {conv_float(d1)} {sign} {conv_float(d2)}")
    print(f"Δ = \033[1m{conv_float(discriminant)}\033[0m\n")
    return discriminant


def discriminant3_negative(formula, discriminant, q):
    """Calculates and prints the solution when the discriminant is negative."""

    a = formula["x3"]
    b = formula["x2"]

    print("Roots of a cubic equation:")
    alpha = (-q / 2 + discriminant ** 0.5) ** (1 / 3)
    beta = (-q / 2 - discriminant ** 0.5) ** (1 / 3)
    print(f"\033[3mα\033[0m = \u221B(-({conv_float(q)}) / "
          f"2 + ({conv_float(discriminant)})^2)")
    print(f"\033[3mβ\033[0m = \u221B(-({conv_float(q)}) / "
          f"2 - ({conv_float(discriminant)})^2)\n")

    x1 = alpha + beta - b / (3 * a)
    x2 = -(alpha + beta) / 2 - b / (3 * a) + (alpha - beta) * 3 ** 0.5 / 2j
    x3 = -(alpha + beta) / 2 - b / (3 * a) - (alpha - beta) * 3 ** 0.5 / 2j

    print(f"X1 = \033[3mα\033[0m + \033[3mβ\033[0m - {conv_float(b)} /"
          f" (3 * {conv_float(a)})")
    print(f"X2 = -(\033[3mα\033[0m + \033[3mβ\033[0m) / 2 - {conv_float(b)} /"
          f" (3 * {conv_float(a)}) + (\033[3mα\033[0m - "
          f"\033[3mβ\033[0m) * \u221A3/ 2i")
    print(f"X3 = -(\033[3mα\033[0m + \033[3mβ\033[0m) / 2 - {conv_float(b)} /"
          f" (3 * {conv_float(a)}) - (\033[3mα\033[0m - "
          f"\033[3mβ\033[0m) * \u221A3/ 2i\n")

    x1 = round(x1.real, 10)
    x2 = round(x2.real, 10)
    x3 = round(x3.real, 10)

    print("\033[35mThe solutions are:\033[0m")
    print(f"X1 = \033[35m\033[1m{conv_float(x1)}\033[0m")
    print(f"X2 = \033[35m\033[1m{conv_float(x2)}\033[0m")
    print(f"X3 = \033[35m\033[1m{conv_float(x3)}\033[0m\n")


def discriminant3_zero(formula, q):
    """Calculates and prints the solution when the discriminant is zero."""

    a = formula["x3"]
    b = formula["x2"]
    if q >= 0:
        x1 = -2 * q ** (1 / 3) - b / (3 * a)
        x2 = q ** (1 / 3) - b / (3 * a)
        print(f"X1 = -2 * \u221B({conv_float(q)}) - ({conv_float(b)}) / "
              f"(3 * ({conv_float(a)}))")
        print(f"X2 = X3 = \u221B({conv_float(q)}) - ({conv_float(b)}) / "
              f"(3 * ({conv_float(a)}))\n")
    else:
        x1 = q ** (1 / 3) - b / (3 * a)
        x2 = -(q ** (1 / 3) + b / (3 * a)) / 2
        print(f"X1 = \u221B({conv_float(q)}) - ({conv_float(b)}) / "
              f"(3 * ({conv_float(a)}))")
        print(f"X2 = X3 = -(\u221B({conv_float(q)}) + ({conv_float(b)}) / "
              f"(3 * ({conv_float(a)})) / 2)\n")

    print("\033[35mThe solutions are:\033[0m")
    if x1 == x2:
        print(f"X1 = X2 = X3 = \033[35m\033[1m{conv_float(x1)}\033[0m\n")
    else:
        print(f"X1 = \033[35m\033[1m{conv_float(x1)}\033[0m")
        print(f"X2 = X3 = \033[35m\033[1m{conv_float(x2)}\033[0m\n")


def discriminant3_positive(formula, discriminant, q):
    """Calculates and prints the solution when the discriminant is positive."""
    a = formula["x3"]
    b = formula["x2"]

    print("Roots of a cubic equation:")
    r = -q / 2 + (discriminant * 0.5)
    s = -q / 2 - (discriminant * 0.5)
    print(f"\033[3mr\033[0m = -({conv_float(q)}) / 2 + "
          f"({conv_float(discriminant)}) / 2")
    print(f"\033[3ms\033[0m = -({conv_float(q)}) / 2 - "
          f"({conv_float(discriminant)}) / 2")
    u = r**(1/3) if r >= 0 else -(-r)**(1/3)
    v = s**(1/3) if s >= 0 else -(-s)**(1/3)

    if r >= 0:
        print(f"\033[3mu\033[0m = \u221B{conv_float(r)}")
    else:
        print(f"\033[3mu\033[0m = -\u221B{conv_float(-r)}")

    if s >= 0:
        print(f"\033[3mv\033[0m = \u221B{conv_float(s)}\n")
    else:
        print(f"\033[3mv\033[0m = -\u221B{conv_float(-s)}\n")

    x1 = u + v - b / (3 * a)
    # x2 = -(u + v) / 2 - b / (3 * a) + (u - v) * 3 ** 0.5 / 2j
    # x3 = -(u + v) / 2 - b / (3 * a) - (u - v) * 3 ** 0.5 / 2j

    sign1 = '+' if v >= 0 else '-'
    sign2 = '-' if b / a >= 0 else '+'
    print(f"X1 = {conv_float(u)} {sign1} {conv_float(abs(v))} {sign2} "
          f"{conv_float(abs(b))} / (3 * {conv_float(abs(a))})")
    print(f"X2 = -({conv_float(u)} {sign1} {conv_float(abs(v))}) / 2 "
          f"{sign2} {conv_float(abs(b))} / (3 * {conv_float(abs(a))}) + "
          f"({conv_float(u)} {sign1} {conv_float(abs(v))}) * \u221A3 / 2i")
    print(f"X3 = -({conv_float(u)} {sign1} {conv_float(abs(v))}) / 2 "
          f"{sign2} {conv_float(abs(b))} / (3 * {conv_float(abs(a))}) - "
          f"({conv_float(u)} {sign1} {conv_float(abs(v))}) * \u221A3 / 2i\n")

    x1 = round(x1.real, 10)
    x2p1 = -(u + v) / 2 - b / (3 * a)
    x2p2 = (u - v) * 3 ** 0.5 / 2j

    print("\033[35mThe solutions are:\033[0m")
    print(f"X1 = \033[35m\033[1m{conv_float(x1)}\033[0m")

    print(f"X2 = \033[35m\033[1m{conv_float(x2p1)} + ({(x2p2)})\033[0m")
    print(f"X3 = \033[35m\033[1m{conv_float(x2p1)} - ({(x2p2)})\033[0m\n")
