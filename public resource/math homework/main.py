def main():
    list_data = []
    with open("math home work.txt","r") as fd:
        data = fd.readlines()

        for formula in data:
            formula_list = formula.split()

            result = my_caculator_conver_to_String(int(formula_list[0]), int(formula_list[2]), formula_list[1])
            new_formula = formula.replace("\n", '')

            new_formula = new_formula + result + '\n'
            print(new_formula)
            list_data.append(new_formula)

    with open("math home work answer.txt", "w") as fd:
        fd.writelines(list_data)


def my_caculator_conver_to_String(First, Second, operator):
    if operator == "*":
        return str(First * Second)
    elif operator == "+":
        return str(First + Second)
    elif operator == "-":
        return str(First - Second)
    elif operator == "/":
        return str(First / Second)


main()





