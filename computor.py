import sys
from equation_parser import argv_parser
from output_formatter import output_forms



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
        output_forms(formula)

    except IndexError:
        print("IndexError") #DELETE
        print ("Entry don't have the right format!")



if __name__ == "__main__":
	main(sys.argv)