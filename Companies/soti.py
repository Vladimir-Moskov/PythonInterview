########## task 1 ####################
left_parenthes = '('
right_parenthes = ')'


def max_valid_paranteses(input1):
    result = 0
    given_str = input1
    left = 0
    right = 0

    for i in range(len(given_str)):
        if given_str[i] == left_parenthes:
            left += 1
        else:
            right += 1
        if left == right:
            result = max(result, 2 * right)
        elif right >= left:
            left = 0
            right = 0

    left = 0
    right = 0
    for i in range(len(given_str) - 1, -1, -1):
        if given_str[i] == left_parenthes:
            left += 1
        else:
            right += 1
        if left == right:
            result = max(result, 2 * right)
        elif left >= right:
            left = 0
            right = 0

    return result

val = "(((("
# print(max_valid_paranteses(val)) # 0
val = "(((()(((("
# print(max_valid_paranteses(val)) # 2


########## task 2 ####################

def coins_find(input1, input2, input3):
    coins = input1
    coins_len = input2
    target_val = input3
    coins.sort()

    result_calculations = [target_val + 1] * (target_val + 1)
    result_calculations[0] = 0
    for i in range(0, coins_len):
        current_coin = coins[i]
        for j in range(current_coin, target_val + 1):
            result_calculations[j] = min(result_calculations[j], result_calculations[j - current_coin] + 1)
    result = result_calculations[-1]
    result_nominals = []
    i = coins_len - 1
    coin = coins[i]
    ind = target_val
    while i >= 0:
        if result_calculations[ind - coin] == result - 1:
            result_nominals.append(coin)
            result -= 1
            ind -= coin
        else:
            i -= 1
            coin = coins[i]

    return result_nominals

print(coins_find([1, 5, 10, 25], 4, 66))  # 5
print(coins_find([1, 4, 6, 30, 100], 5, 99))  # 6
