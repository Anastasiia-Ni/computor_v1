from output_formatter import output_polynomial_degree
from solve_quadratic import solve_quadratic_equation
from solve_cubic import solve_cubic_equation
from utils import irreducible_fraction, print_one_fraction


def conv_float(num):
    return int(num) if float(num).is_integer() else round(num, 4)


def addition_monomials(formula):
    if formula["x0"]:
        print("\033[35mThis equation has \033[1mno solutions\033[0m "
              "\033[35mas it is false.\033[0m\n")
    else:
        print("\033[35mThis equation is an \033[1midentity.\033[0m")
        print("\033[35mAn identity is a statement that is \033[1mtrue "
              "for all values\033[0m \033[35mof the variables.\033[0m\n")


def solve_linear_equation(formula):
    result = -formula["x0"] / formula["x1"]
    result = conv_float(result)
    print(f"\033[35m\033[1mX \033[0m\033[35m= {conv_float(-formula['x0'])} / "
          f"{conv_float(formula['x1'])}\n")
    print(f"The solution is: \033[1m{result}\033[0m\n")

    if ir_fract := irreducible_fraction(-formula["x0"], formula["x1"]):
        print_one_fraction(ir_fract)


def solve_method(formula):
    # next() используется для получения первого элемента, по условию
    polynom = \
        next((i for i in range(len(formula)-1, -1, -1) if formula[f'x{i}']), 0)

    output_polynomial_degree(polynom)

    solutions = {
        0: addition_monomials,
        1: solve_linear_equation,
        2: solve_quadratic_equation,
        3: solve_cubic_equation,
    }

    solutions.get(polynom)(formula)
