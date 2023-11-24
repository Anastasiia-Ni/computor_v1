from output_formatter import output_polynomial_degree
from solve_quadratic import solve_quadratic_equation
from solve_cubic import solve_cubic_equation


def conv_float(num):
    return int(num) if float(num).is_integer() else round(num, 4)


def addition_monomials(formula):
    if formula["x0"]:
        print("это уравнение не имеет решений, так как оно неверно")
    else:
        print("Это уравнение представляет собой тождество (identity) ")
        print("Тождество - это утверждение, которое истинно для всех значений переменных.")


def solve_linear_equation(formula):
    result = -formula["x0"] / formula["x1"]
    result = conv_float(result)
    print(f"The solution is: {result}")
    pass


def solve_method(formula):
    # next() используется для получения первого элемента, удовлетворяющего условию
    polynom = next((i for i in range(len(formula)-1, -1, -1) if formula[f'x{i}']), 0)
    
    output_polynomial_degree(polynom)

    solutions = {
        0: addition_monomials,
        1: solve_linear_equation,
        2: solve_quadratic_equation,
        3: solve_cubic_equation,
    }

    solutions.get(polynom)(formula)