"""

"""


def encode_4twist(str_val):
    twist_size = 4
    start_position = 0
    result = [0] * twist_size

    while start_position < len(str_val):
        end_pos = start_position + twist_size
        end_pos = end_pos if end_pos < len(str_val) else len(str_val)
        dif = twist_size - end_pos - start_position
        for i in range(start_position, end_pos):
            result[- 1 - i] = (ord(str_val[i]))

        for i in range(dif):
            result[i] = 0

        result_2 = list(map(bin, result))
        val_ar = [0] * twist_size
        for k in range(twist_size):
            val_mask = 0b10000000
            shift = 0
            for i in range(2):
                for j in range(twist_size):
                    v = (result[j] & val_mask)
                    v = v >> shift
                    shift += 1
                    val_ar[k] = val_ar[k] | v
                    result[j] = result[j] << 1
                #val_mask = val_mask >> 1


        start_position = end_pos
        result_3 = list(map(bin, val_ar))
        result_int = 0
        for i, val in enumerate(val_ar):
            result_int = result_int | (val << (8 * (3 - i)))
    return result

# case 1
str_val = "A"

# case 2
str_val = "FRED"

# case 3
str_val = " :^)"

# case 4
str_val = "a@b." # 131107009
str_val = "foo"
str_val = "boba"
print(encode_4twist(str_val))

# "foo" 124807030
# " foo" 250662636
# "foot" 267939702
# "BIRD" 251930706
# "...." 15794160
# "^^^^" 252706800
# "Woot" 266956663
# "no" 53490482
