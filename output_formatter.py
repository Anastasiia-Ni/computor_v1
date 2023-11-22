
# Вывод уравнения в упрощенной форме.
def output_reduced_form(formula):
    reduced_form = ""

    coefficients = [formula[f'x{i}'] for i in range(4)]
    for i, coef in enumerate(coefficients):
        # Преобразовываем флоаты в целые числа, если после точки нет чисел
        coef = int(coef) if float(coef).is_integer() else coef
        if coef > 0 and i == 0:
            reduced_form += f"{coef} * X^{i} "
        elif coef > 0 and i > 0:
            reduced_form += f"+ {coef} * X^{i} "
        elif coef < 0:
            reduced_form += f"- {abs(coef)} * X^{i} " # пробел после знака -
        # else:   # case 0 пока мешает, потом может верну
        #     if i == 0:
        #         reduced_form += f"{coef} * X^{i} "
        #     elif i < 3:
        #         reduced_form += f"+ {coef} * X^{i} "


    reduced_form += "= 0"

    print(f"Reduced form: {reduced_form}")
    


# Вывод степени полинома.
def output_polynomial_degree(polynom):

    print(f"Polynomial degree: {polynom}")
    # print("The polynomial degree is strictly greater than 2, I can't solve.")


# Вывод решений и информации о дискриминанте (для квадратных уравнений).
def output_discriminant():
    pass
    


def output_solution(discriminant, answer):
    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        print(answer[0])
        print(answer[1])
    if discriminant == 0:
        print("The solution is:")
        print(answer[0])


# Вывод промежуточных шагов. (для бонуса)
def output_intermediate_steps():
    pass

# def output_forms(formula):

