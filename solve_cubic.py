from utils import conv_float
# formula = {"x0":0, "x1": 0, "x2": 0, "x3": 0}


def solve_discriminant3(a, b, c, d):
    print("Calculate the discriminants:")
    d0 = b**2 - 3 * a * c
    d1 = b**3 * 2 - 9 * a * b * c + a**2 * 27 * d

    print(f"Δ0 = ({b})^2 - 3 * ({a}) * ({c})")
    print(f"Δ1 = 2 * ({b})^3 - 9 * ({a}) * ({b}) * ({c}) + 27 * ({a})^2 * ({d})")

    d1p2 = 3 * a * c
    d2p2 = 9 * a * b * c
    d2p3 = 27*a**2*d

    sign1 = '+' if d1p2 < 0 else '-'
    d1p2 = abs(d1p2)

    sign2 = '+' if d2p2 < 0 else '-'
    d2p2 = abs(d2p2)

    sign3 = '-' if d2p3 < 0 else '+'
    d2p3 = abs(d2p3)

    print(f"Δ0 = {conv_float(b**2)} {sign1} {conv_float(d1p2)}")
    print(f"Δ1 = {conv_float(b**3 * 2)} {sign2} {conv_float(d2p2)} {sign3} {conv_float(d2p3)}")

    print(f"Δ0 = {conv_float(d0)}")
    print(f"Δ1 = {conv_float(d1)}")

    return d0, d1


def solve_case4(a, b, c, d, d0, d1):
    p = d0 / (3 * a**2)
    q = d1 / (27 * a**3)
    discriminant = q**2 / 4 + p**3 / 27
    print(p)
    print(q)
    print(discriminant)


# метод Кардано
def solve_cubic_equation(formula):
    print("The solutions (Cardano's Method) are:")
    a = formula["x3"]
    b = formula["x2"]
    c = formula["x1"]
    d = formula["x0"]

    d0, d1 = solve_discriminant3(a, b, c, d)

    if d0 > 0 and d1 > 0:
        print("У уравнения три вещественных корня.")
        # solve_case1(a, b, c, d, d0, d1)
    elif d0 > 0 and d1 < 0:
        print("У уравнения один вещественный корень и два комплексных корня.")
        # solve_case2(a, b, c, d, d0, d1)
    elif d0 > 0 and d1 == 0:
        print("Этот случай не произойдет")
        # solve_case3(a, b, c, d, d0, d1)
    elif d0 < 0 and d1 > 0:
        print("У уравнения один вещественный корень и два комплексных корня.")
        solve_case4(a, b, c, d, d0, d1)
    elif d0 < 0 and d1 < 0:
        print("У уравнения один вещественный корень и два комплексных корня.")
        # solve_case5(a, b, c, d, d0, d1)
    elif d0 < 0 and d1 == 0:
        print("У уравнения один вещественный корень и два комплексных корня.")
        # solve_case6(a, b, c, d, d0, d1)
    elif d0 == 0 and d1 > 0:
        print("Этот случай не произойдет")
    elif d0 == 0 and d1 < 0:
        print("У уравнения один вещественный корень и два комплексных корня.")
        # solve_case8(a, b, c, d, d0, d1)
    elif d0 == 0 and d1 == 0:
        print("У уравнения три кратных корня")
        # solve_case9(a, b, c, d, d0, d1)
