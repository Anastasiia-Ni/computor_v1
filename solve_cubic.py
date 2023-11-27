from utils import conv_float, irreducible_fraction, print_one_fraction
import cmath 
# formula = {"x0":0, "x1": 0, "x2": 0, "x3": 0}
import numpy as np


def solve_cubic_equation(formula):
    a = formula["x3"]
    b = formula["x2"]
    c = formula["x1"]
    d = formula["x0"]
    # coefficients = [a, b, c, d]
    # roots = np.roots(coefficients)


    # delta0 = b**2 - 3*a*c
    # delta1 = 2*b**3 - 9*a*b*c + 27*a**2*d

    # # Вычисляем корень кубического уравнения
    # C = ((delta1 + cmath.sqrt(delta1**2 - 4*delta0**3)) / 2)**(1/3)

    # # Вычисляем корни кубического уравнения
    # x1 = -1/(3*a) * (b + C + delta0/C)
    # x2 = -1/(3*a) * (b + cmath.exp(2j * cmath.pi / 3) * C + delta0/(cmath.exp(2j * cmath.pi / 3) * C))
    # x3 = -1/(3*a) * (b + cmath.exp(4j * cmath.pi / 3) * C + delta0/(cmath.exp(4j * cmath.pi / 3) * C))
    
    # x1 = round(x1.real, 10)
    # x2 = round(x2.real, 10)
    # x3 = round(x3.real, 10)

    # print(f"X1 = {x1}")
    # print(f"X2 = {x2}")
    # print(f"X3 = {x3}")

    print("\033[35mCoefficients for calculating the discriminant:\033[0m")
    
    p = (3 * a * c - b * b) / (3 * a * a)
    print(f"Cubic Cauchy Coefficient:\033[0m")
    print(f"\033[3mp\033[0m = (3 * ({conv_float(a)}) * ({conv_float(c)}) - "
            f"({conv_float(b)})^2) / (3 * ({conv_float(a)})^2)")
    print(f"\033[3mp\033[0m = \033[1m{conv_float(p)}\033[0m")

    q = (2 * b * b * b - 9 * a * b * c + 27 * a * a * d) / (27 * a * a * a)
    print(f"Cubic Viète Coefficient:\033[0m")
    print(f"\033[3mq\033[0m = (2 * ({conv_float(b)})^3 - 9 * "
          f"({conv_float(a)}) * ({conv_float(b)}) * ({conv_float(c)}) + "
          f"27 * ({conv_float(a)})^2 * ({conv_float(d)})) / "
          f"(27 * ({conv_float(a)})^3)")
    print(f"\033[3mq\033[0m = \033[1m{conv_float(q)}\033[0m\n")
    

    discriminant = solve_discriminant3(p, q)
    
    if discriminant > 0:
        r = -q/2 + (discriminant * 0.5)
        s = -q/2 - (discriminant * 0.5)
        print(r)
        print (s)
        u = r**(1/3) if r >= 0 else -(-r)**(1/3)
        v = s**(1/3) if s >= 0 else -(-s)**(1/3)
        print (u)
        print (v)
        x1 = u + v - b/(3*a)
        x2 = -(u + v)/2 - b/(3*a) + (u - v)*cmath.sqrt(3)/2j
        x3 = -(u + v)/2 - b/(3*a) - (u - v)*cmath.sqrt(3)/2j
        print("Реальный корень: x1 =", x1)
        print("Комплексные корни: x2 =", x2, "и x3 =", x3)
    elif discriminant == 0:
        if q >= 0:
            x1 = -2*q**(1/3) - b/(3*a)
            x2 = q**(1/3) - b/(3*a)
            print("Все три корня реальны, два из них совпадают: x1 =", x1, "и x2 = x3 =", x2)
        else:
            x1 = q**(1/3) - b/(3*a)
            x2 = x3 = -(q**(1/3) + b/(3*a))/2
            print("Все три корня реальны, два их них совпадают: x1 =", x1, "и x2 = x3 =", x2)
    else:
        print("\033[35mThe discriminant is negative, the equation has three real solutions.\033[0m")
        discriminant3_positive(formula, discriminant, q)



def solve_discriminant3(p, q):
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



def discriminant3_positive(formula, discriminant, q):
    a = formula["x3"]
    b = formula["x2"]

    print("Roots of a cubic equation:")
    alpha = (-q / 2 + discriminant ** 0.5) ** (1 / 3)     
    beta = (-q / 2 - discriminant ** 0.5) ** (1 / 3)
    print(f"\033[3mα\033[0m = \u221B(-({conv_float(q)}) / 2 + ({conv_float(discriminant)})^2)")
    print(f"\033[3mβ\033[0m = \u221B(-({conv_float(q)}) / 2 - ({conv_float(discriminant)})^2)\n")

    x1 = alpha + beta - b / (3 * a)
    x2 = -(alpha + beta) / 2 - b / (3 * a) + (alpha - beta) * cmath.sqrt(3) / 2j
    x3 = -(alpha + beta) / 2 - b / (3 * a) - (alpha - beta) * cmath.sqrt(3) / 2j

    print(f"X1 = \033[3mα\033[0m + \033[3mβ\033[0m - {conv_float(b)} /"
            f" (3 * {conv_float(a)})")
    print(f"X2 = -(\033[3mα\033[0m + \033[3mβ\033[0m) / 2 - {conv_float(b)} /"
            f" (3 * {conv_float(a)}) + \u221B(\033[3mα\033[0m - "
            f"\033[3mβ\033[0m) / 2i")
    print(f"X3 = -(\033[3mα\033[0m + \033[3mβ\033[0m) / 2 - {conv_float(b)} /"
            f" (3 * {conv_float(a)}) - \u221B(\033[3mα\033[0m - "
            f"\033[3mβ\033[0m) / 2i")

    x1 = round(x1.real, 10)
    x2 = round(x2.real, 10)
    x3 = round(x3.real, 10)

    print("\033[35mThe solutions are:\033[0m")
    print(f"X1 = \033[35m\033[1m{conv_float(x1)}\033[0m")
    print(f"X2 = \033[35m\033[1m{conv_float(x2)}\033[0m")
    print(f"X3 = \033[35m\033[1m{conv_float(x3)}\033[0m\n")
