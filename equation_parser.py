
def argv_check(input_str):
    
    if input_str.count('=') != 1:
        return False
    for i, char in enumerate(input_str):
        if char not in set("0123456789^.*=+-X"):
            return False
        if char == '*' and i < len(input_str) - 1 and input_str[i + 1] != 'X':
            return False
        if char in ('-', '+') and i < len(input_str) - 1:
            if not input_str[i + 1].isdigit() and input_str[i + 1] !='X':
                return False
        if char in set("+-*=") and i == len(input_str) - 1:
            return False
        if char == '^':
            if i > 0 and input_str[i - 1] != 'X':
                return False
            if i < len(input_str) - 1 and input_str[i + 1] not in set('0123'):
                return False
            if i == 0 or i == len(input_str) - 1:
                return False
            if i < len(input_str) - 2 and input_str[i + 2] not in set('+-='):
                return False
        if (char == '=' or char == '*') and i == 0:
            return False
        if char == '.' and i > 0 and input_str[i - 1] == '.':
            return False
        if char == 'X' and i > 0 and input_str[i - 1] not in set('*+-='):
            return False

    return True


def split_equation(part_str):
    equation_parts = part_str.split('+')
    split_parts = []

    for part in equation_parts:
        parts_with_minus = part.split('-')
        for i, sub_part in enumerate(parts_with_minus):
            if i == 0:
                split_parts.append(sub_part)
            else:
                split_parts.append('-' + sub_part)
    
    return split_parts


def argv_parser(arg_str):
    print("PARSING START")
    formula = {"x0": 0, "x1": 0, "x2": 0, "x3": 0}

    sides_equation = arg_str.split('=')

    left_side = split_equation(sides_equation[0])
    right_side = split_equation(sides_equation[1])

    print(left_side) #DELETE
    print(right_side) #DELETE

    for s in left_side:
        index = s.find("*X^")
        if (index > 0):
            num = float(s[:index])
            index += 3
            order = int(s[index])
            formula[f'x{order}'] += num
        else:
            index_any = s.find("X^")
            if index_any >= 0:
                order = int(s[index_any + 2])
                formula[f'x{order}'] += 1
            else:
                index1 = s.find("X")
                if index1 == 0:
                    formula['x1'] += 1
                elif index1 > 0 :
                    num = float(s[:index - 1])
                    formula['x1'] += num
                elif s:
                    num = float(s)
                    formula['x0'] += num

    for s in right_side:
        index = s.find("*X^")
        if (index > 0):
            num = float(s[:index])
            index += 3
            order = int(s[index])
            formula[f'x{order}'] -= num
        else:
            index_any = s.find("X^")
            if index_any >= 0:
                order = int(s[index_any + 2])
                formula[f'x{order}'] -= 1
            else:
                index1 = s.find("X")
                if index1 == 0:
                    formula['x1'] -= 1
                elif index1 > 0 :
                    num = float(s[:index - 1])
                    formula['x1'] -= num
                elif s:
                    num = float(s)
                    formula['x0'] -= num

    return formula
    