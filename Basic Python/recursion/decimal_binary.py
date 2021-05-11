"""
Write a Python program that converts a decimal number to binary using recursion.

The function must return the binary representation as a string.

The program must print the value returned.
"""

def convert_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    else:
        return (convert_to_binary(decimal_num // 2) + str(decimal_num % 2)).lstrip("0")

print(convert_to_binary(5))
print(bin(5))