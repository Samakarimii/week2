def decimal_to_binary(decimal_num):
    binary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2 # decimal_num = decimal_num // 2
    return binary_num

decimal_num = int(input("please enter your number "))
binary_num = decimal_to_binary(decimal_num)
print( binary_num)
    