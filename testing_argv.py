from equation_parser import argv_check

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'


def testing():
    bad_strs = [
    "11 * X^0 + 7 * X^1 = 77 * X^0 = 8 * X^1",
    "11 * X^0 + 7 * X^1 = * ",
    "11 * X^0 + 7 * X^1 = + ",
    "6 * X^15 - 4 * X^0 = 14 * X^0",
    "6 * X^1 - + 4 * X^0 = 14 * X^0",
    "6 * X^1 * 4 * X^0 = 14 * X^0",
    "6 * X^^1 * 4 * X^0 = 14 * X^0",
    "6 * X^1 * 4 * X^0 = ^0",
    "6 * X^1 * 4 * X^0 = ",
    " = 14 * X^0",
    "6 * X^1. - + 4 * X^0 = 14 * X^0",
    "6 * X^1 - 4..3 * X^0 = 14 * X^0",
    "5 * X^0 + 4 * Y^1 = 0",
    "5 * X^0 + 4 * X^1 = 0$",
    "5 * X^0 + 4 * X^1",
    "* X^1 - 4 * X^0 = -14 * X^0",
    "42 * X^0 = 42 * X^",
    "42 * X^0 = 42 * X^*",
    "^0 = 42 * X^0",
    "6 * X^1 - 4 * X^0 = +",
    ".5 + 4 * X + X^2= X^2.",
     "5X + X^2= X^2",
    ]
    print("Bad cases:")
    for arg_str in bad_strs:
        result = argv_check(arg_str.upper().replace(" ", ""))
        status = f'{GREEN}✓{RESET}' if not result else f'{RED}✗{RESET}'
        print(f'"{arg_str}": {result} : {status}')

    good_cases = [
        "42 * X^0 = 42 * X^0",
        "6 * X^1 - 4 * X^0 = -14 * X^0",
        "5 * X^0 + 4 * X^1 = 0",
        "1 * X^3 - 7 * X^2 + 11 * X^1 - 2 * X^0 = 0",
        "3 * X^3 - 7 * X^2 - 7 * X^1 + 3 * X^0 = 0",
        "-5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
        "5 + 4 * X + X^2= X^2",
        ".5 + X + X^2= X^2",
        "X + X^2= X^2",

    ]
    print("Good cases:")
    for arg in good_cases:
        result = argv_check(arg.upper().replace(" ", ""))
        status = f'{GREEN}✓{RESET}' if result else f'{RED}✗{RESET}'
        print(f'"{arg}": {result} : {status}')


testing()
