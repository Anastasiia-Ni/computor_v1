
# Вывод уравнения в упрощенной форме.
def output_reduced_form(formula):
    print(f"Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0")
    


# Вывод степени полинома.
def output_polynomial_degree(formula):
    print(f"Polynomial degree: ")
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