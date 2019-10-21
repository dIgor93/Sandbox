def get_var_name(n):
    name = str(chr(ord('a') + n))
    return name


def reverse_polish(pos, exp_list):
    curr_char = str(exp_list[pos])
    if curr_char == '?':
        if reverse_polish(pos - 3, exp_list):
            res = reverse_polish(pos - 2, exp_list)
        else:
            res = reverse_polish(pos - 1, exp_list)
        start = pos - 3
        end = None if pos == -1 else pos + 1
        exp_list[start:end] = [res]
        return res
    elif curr_char in '+-*/<=':
        b = reverse_polish(pos - 1, exp_list)
        a = reverse_polish(pos - 2, exp_list)
        if curr_char == '+':
            res = a + b
        elif curr_char == '-':
            res = a - b
        elif curr_char == '/':
            res = a / b
        elif curr_char == '*':
            res = a * b
        elif curr_char == '<':
            res = a < b
        elif curr_char == '=':
            res = a == b
        else:
            res = 0
        start = pos - 2
        end = None if pos == -1 else pos + 1
        exp_list[start:end] = [res]
        return res
    else:
        return exp_list[pos]


def main():
    with open('input.txt', 'r') as file:
        int(file.readline())
        formula = file.readline().strip()
        test_count = int(file.readline())
        tests_vars = []
        for i in range(test_count):
            vars = dict(map(lambda x: (get_var_name(x[0]), int(x[1])), enumerate(file.readline().split())))
            tests_vars.append(vars)

        for vars in tests_vars:
            new_formula = formula
            for name, value in vars.items():
                new_formula = new_formula.replace(str(name), str(value))
            formula_list = [x if x in '+-/*<=?' else int(x) for x in new_formula.split()]
            print(reverse_polish(-1, formula_list))


if __name__ == '__main__':
    main()
