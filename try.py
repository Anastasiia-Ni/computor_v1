import sys
from computor import main

# Zero
# formula = "42 * X^0 = 42 * X^0"
# formula = "42 * X^0 = 4 * X^0"

#First
# formula = "6 * X^1 - 4 * X^0 = 14 * X^0"    # X = 3
# formula = "5 * X^1 - 18 * X^0 = 2 * X^1"    # X = 6
# formula = "7 * X^1 - 4 * X^0 = 5 * X^1 + 16 * X^0"  # X = 10
# formula = "11 * X^0 + 7 * X^1 = 77 * X^0 + 8 * X^1" # X = -66
# formula = "5 * X^0 + 4 * X^1 = 4 * X^0" #  X = -0.25
# formula = "20 * X^1 - 28 * X^0 - 24 * X^0 = 9 * X^1 + 36 * X^0" #  X = 8
# formula = "5 * X^1 - 15 * X^0 + 2 * X^0 = 3 * X^1 - 12 * X^0 + 2 * X^1 - 1 * X^0"   # any
# formula = "5 * X^1 - 15 * X^0 + 2 * X^1 = 0"    #, X = 2.1429

#Quadratic
# formula = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" #, X1 = 0.905239, X2 = -0.475131
# formula = "27 * X^0 - 18 * X^1 + 3 * X^2 = 0" # X = 3
# formula = "9 * X^2 + 6 * X^1 = -1" # X = 0.333
# formula = "12 * X^2 = -1 -7 * X^1" # X1 = -0.25, X2 = -0.3333
# formula = "X^2 - 2 * X^1 = -5" # X1 = 1 + 2i, X2 = 1 - 2i
# formula = "X^2 + 6 * X^1 = -14 * X^0" # X1 = -3 + 2.2360i, X2 = -3 - 2.2360i
# formula = "-1 * X^2 - 6 * X^1 = 14 * X^0" # X1 = -3 - 2.2361i, X2 = X2 = -3 + 2.2361i



#Cubic
formula = "1 * X^3 - 7 * X^2 + 11 * X^1 - 2 * X^0 = 0" #  X1 = 2, X2 = 4.791288, X3 = 0,208712
# formula = "1 * X^3 - 7 * X^1 + 6 * X^0 = 0" # X1 = 1, X2 = 2, X3 = -3
# formula = "3 * X^3 - 7 * X^2 - 7 * X^1 + 3 * X^0 = 0" # X1 = -1, X2 = 3, X3 = 0.333333


#invalid cases

# formula = "11 * X^0 + 7 * X^1 = 77 * X^0 = 8 * X^1"
# formula = "* X^0 + 7 * X^1 = 77 * X^0 + 8 * X^1"
# formula = "6 * X^15 - 4 * X^0 = 14 * X^0"
# formula = "6 * X^1 - + 4 * X^0 = 14 * X^0"
# formula = "6 * X^1 * 4 * X^0 = 14 * X^0"
# formula = "6 * X^^1 * 4 * X^0 = 14 * X^0"
# formula = "6 * X^1 * 4 * X^0 = ^0"
# formula = "6 * X^1 * 4 * X^0 = "
# formula = " = 14 * X^0"
# formula = "6 * X^1. - + 4 * X^0 = 14 * X^0"
# formula = "6 * X^1 - + 4..3 * X^0 = 14 * X^0"



arguments = ["computor.py", formula]

main(arguments)