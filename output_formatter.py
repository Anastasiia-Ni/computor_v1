
# Вывод уравнения в упрощенной форме.
def output_reduced_form(formula):
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


def print_intermediate_form(f_list):
    # f_list = {"x0": [], "x1": [], "x2": [], "x3": []}
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
    s = len(expression) + 20
    print(f"\033[32m{s * '-'}\033[0m")
    print(f"\033[32mIntermediate form: \033[1m{expression}\033[0m")
    print(f"\033[32m{s * '-'}\033[0m\n")


# Вывод степени полинома.
def output_polynomial_degree(polynom):
    print(f"\033[33mPolynomial degree: \033[1m{polynom}\033[0m\n")
    # print("The polynomial degree is strictly greater than 2, I can't solve.")


def output_solution(discriminant, answer):
    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        print(answer[0])
        print(answer[1])
    if discriminant == 0:
        print("The solution is:")
        print(answer[0])
