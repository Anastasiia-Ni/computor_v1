import sys
from equation_parser import argv_parser
from output_formatter import output_reduced_form
from equation_solver import solve_method



def main(argv):
    if len(argv) == 1:
        print("There must be one argument")
        return
    elif len(argv) != 2:
        print("Must be only one argument")
        return

    try:
    # check argv
        formula = argv_parser(argv[1])
        output_reduced_form(formula)
        solve_method(formula)



    except IndexError:
        print("IndexError") #DELETE
        print ("Entry don't have the right format!")
    except ZeroDivisionError:
        print("ZeroDivisionError")



if __name__ == "__main__":
	main(sys.argv)