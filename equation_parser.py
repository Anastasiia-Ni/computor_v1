from output_formatter import print_full_form


def argv_check(str):
    if str.count('=') != 1:
        return False
    for i, char in enumerate(str):
        if char not in set("0123456789^.*=+-X"):
            return False
        if char == '*' and i < len(str) - 1 and str[i + 1] != 'X':
            return False
        if char in ('-', '+') and i < len(str) - 1:
            if not str[i + 1].isdigit() and str[i + 1] != 'X':
                return False
        if char in set("+-*=") and i == len(str) - 1:
            return False
        if char == '^':
            if i > 0 and str[i - 1] != 'X':
                return False
            if i < len(str) - 1 and str[i + 1] not in set('0123'):
                return False
            if i == 0 or i == len(str) - 1:
                return False
            if i < len(str) - 2 and str[i + 2] not in set('+-='):
                return False
        if (char == '=' or char == '*') and i == 0:
            return False
        if char == '.' and i > 0 and str[i - 1] == '.':
            return False
        if char == 'X':
            if i > 0 and str[i - 1] not in set('*+-='):
                return False
            elif i < len(str) - 1 and str[i + 1] not in set('^=+-'):
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


def parse_sides(f_list, side, p):
    for s in side:
        index = s.find("*X^")
        if (index > 0):
            num = float(s[:index])
            index += 3
            order = int(s[index])
            f_list[f'x{order}'].append(num) if p == 'l' else f_list[f'x{order}'].append(-num)
        else:
            index_any = s.find("X^")
            if index_any == 0:
                order = int(s[index_any + 2])
                f_list[f'x{order}'].append(1) if p == 'l' else f_list[f'x{order}'].append(-1)
            elif index_any == 1 and s[0] == '-':
                order = int(s[index_any + 2])
                f_list[f'x{order}'].append(-1) if p == 'l' else f_list[f'x{order}'].append(1)
            else:
                index1 = s.find("X")
                if index1 == 0:
                    f_list['x1'].append(1) if p == 'l' else f_list['x1'].append(-1)
                elif index1 == 1 and s[0] == '-':
                    f_list['x1'].append(-1) if p == 'l' else f_list['x1'].append(1)
                elif index1 > 0:
                    num = float(s[:index - 1])
                    f_list['x1'].append(num) if p == 'l' else f_list['x1'].append(-num)
                elif s:
                    num = float(s)
                    f_list['x0'].append(num) if p == 'l' else f_list['x0'].append(-num)


def argv_parser(arg_str):
    f_list = {"x0": [], "x1": [], "x2": [], "x3": []}
    # formula = {"x0": 0, "x1": 0, "x2": 0, "x3": 0}

    sides_equation = arg_str.split('=')

    left_side = split_equation(sides_equation[0])
    right_side = split_equation(sides_equation[1])

    parse_sides(f_list, left_side, 'l')
    parse_sides(f_list, right_side, 'r')
    print_full_form(f_list)

    # formula = {key: sum(values) for key, values in f_list.items()}
    # return formula
    return {key: sum(values) for key, values in f_list.items()}
