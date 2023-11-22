
def argv_check():
    # count('=') == 1
    # 
    pass

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
    print(arg_str) # DELETE
    formula = {"x0":0, "x1": 0, "x2": 0, "x3": 0}

    arg_str = arg_str.replace(" ", "")
    sides_equation = arg_str.split('=')

    left_side = split_equation(sides_equation[0])
    right_side = split_equation(sides_equation[1])

    for s in left_side:
        index = s.find("*X^")
        if (index > 0):
            num = float(s[:index])
            index += 3
            order = int(s[index])
            formula[f'x{order}'] += num
       
    for s in right_side:
        index = s.find("*X^")
        if (index > 0):
            num = float(s[:index])
            index += 3
            order = int(s[index])
            formula[f'x{order}'] += -num

    return formula

    # print(left_side)
    # print(right_side)







    return formula
    