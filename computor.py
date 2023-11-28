import sys
from equation_parser import argv_parser, argv_check
from output_formatter import output_reduced_form
from equation_solver import solve_method
from utils import print_error


def main(argv):
    if len(argv) == 1:
        print("There must be one argument")
        return
    elif len(argv) != 2:
        print("Must be only one argument")
        return

    try:
        arg_str = argv[1].upper().replace(" ", "")
        if not argv_check(arg_str):
            print_error()
            return
        formula = argv_parser(arg_str)
        output_reduced_form(formula)
        solve_method(formula)

    except IndexError:
        print("IndexError")  # DELETE
        print("Entry don't have the right format!")  # change message
    except ValueError:
        print("Entry don't have the right format!")  # change message
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except TypeError as e:
        print(f"TypeError: {e}")


if __name__ == "__main__":
    main(sys.argv)
