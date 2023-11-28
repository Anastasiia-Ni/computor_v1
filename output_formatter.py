def output_reduced_form(formula):
    """Outputs the equation in its simplified form."""
    reduced_form = ""

    coefficients = [formula[f'x{i}'] for i in range(4)]
    for i, coef in enumerate(coefficients):
        # Преобразовываем флоаты в целые числа, если после точки нет чисел
        coef = int(coef) if float(coef).is_integer() else coef
        if not reduced_form:
            reduced_form += f"{coef} * X^{i} "
        elif coef > 0:
            reduced_form += f"+ {coef} * X^{i} "
        elif coef < 0:
            reduced_form += f"- {abs(coef)} * X^{i} "  # пробел после знака -
        # else:   # case 0 пока мешает, потом может верну
        #     if i == 0:
        #         reduced_form += f"{coef} * X^{i} "
        #     elif i < 3:
        #         reduced_form += f"+ {coef} * X^{i} "

    reduced_form += "= 0"
    s = max(40, len(reduced_form) + 15)
    print(f"\033[33m{s * '-'}\033[0m")
    print(f"\033[33mReduced form: \033[1m{reduced_form}\033[0m")
    print(f"\033[33m{s * '-'}\033[0m")


def print_full_form(f_list):
    """Prints the equation in its full form."""

    expression = ""
    for i, (key, values) in enumerate(f_list.items()):
        for _, value in enumerate(values):
            value = int(value) if float(value).is_integer() else value
            if not expression:
                expression += f"{value} * X^{i} "
            elif value > 0:
                expression += f"+ {value} * X^{i} "
            elif value < 0:
                expression += f"- {abs(value)} * X^{i} "

    expression += "= 0"
    s = len(expression) + 15
    print(f"\033[32m{s * '-'}\033[0m")
    print(f"\033[32mFull form: \033[1m{expression}\033[0m")
    print(f"\033[32m{s * '-'}\033[0m\n")


# Вывод степени полинома.
def output_polynomial_degree(polynom):
    """Outputs the degree of the polynomial."""

    print(f"\033[33mPolynomial degree: \033[1m{polynom}\033[0m\n")
