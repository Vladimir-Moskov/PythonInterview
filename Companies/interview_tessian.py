from typing import Dict, Optional, Tuple
import itertools

operatorTable = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: a // b)
}

def max_result_expression(expression: str, variables: Dict[str, Tuple[int, int]]) -> Optional[int]:
    result = None

    if len(variables.items()) == 0:
        result = one_expression_cals(expression)
    else:
        result_ar = []

        all_list_val = []
        all_list_var = list(variables.keys())
        for item in variables.values():
            all_list_val.append([i for i in range(item[0], item[1])])
        combinations = list(itertools.product(*all_list_val))

        for combination in combinations:
            new_expression = expression
            for j in range(0, len(all_list_var)):
                new_expression = str.replace(new_expression, all_list_var[j], str(combination[j]))
            temp_result = one_expression_cals(new_expression)
            if temp_result:
                result_ar.append(temp_result)
        if len(result_ar) > 0:
            result = max(result_ar)

    return result

def one_expression_cals(expression) -> Optional[int]:
    expression_ar = expression.split()
    result = None
    if validate_expresssion(expression_ar):
        result = expresssion_parser(expression_ar)
        if len(result) != 1:
            result = None
        else:
            result = result[0]

    return result


def expresssion_parser(expression_ar):
    expression_ar.reverse()
    exp_stack = []
    try:
        for operand in expression_ar:
            if operand in operatorTable:
                if len(exp_stack) < 2:
                    return []
                arg1 = exp_stack.pop()
                arg2 = exp_stack.pop()
                result = operatorTable[operand](arg1,  arg2)
                exp_stack.append(result)
            else:
                exp_stack.append(int(operand))
    except:
        exp_stack = []

    return exp_stack


def validate_expresssion(expression):
    is_valid = True
    for i, operand in enumerate(expression):
        if operand in operatorTable:
            pass
        else:
            try:
                int_val = int(operand)
                expression[i] = int_val
            except ValueError:
                is_valid = False
                break

    return is_valid

# print(int("+-1"))

# expression = "+ 1 5"
# variables = {}
# print("max_result_expression: 6​")
# print(max_result_expression(expression, variables))
#
# expression = "+ 1 2 3"
# variables = {}
# print("max_result_expression: None​")
# print(max_result_expression(expression, variables)) #None
# #
# expression = "+ 1"
# variables = {}
# print("max_result_expression: None​")
# print(max_result_expression(expression, variables)) #None
# #
# expression = "9"
# variables = {}
# print("max_result_expression: 9")
# print(max_result_expression(expression, variables)) # 9
# #
# expression = "* + 1 2 3"
# variables = {}
# print("max_result_expression: 9")
# print(max_result_expression(expression, variables)) # 9
# #
# expression = "+ 6
# * - 4 + 2 3 8"
expression = "+ 6 * - 4 + 2 3 8"
variables = {}
print("max_result_expression: -2")
print(max_result_expression(expression, variables)) # -2
# #
# expression = "-+1 5 3"
# variables = {}
# print("max_result_expression: None​")
# print(max_result_expression(expression, variables)) # None
# #
# expression = "+ 1       2"
# variables = {}
# print("max_result_expression: 3")
# print(max_result_expression(expression, variables)) # 3
# #
# expression = "* + 2 x y"
# variables = { "x": (0, 2), "y": (2, 4) }
# #variables = { "x": (0, 3), "y": (2, 5) }
# prit("max_result_expression: 9")
# print(max_result_expression(expression, variables)) # 9n