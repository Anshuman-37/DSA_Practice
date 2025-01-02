# Question 22: Convert integer to Roman numeral and vice versa.
def int_to_roman(num):
    values = [
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    ]
    symbols = [
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    ]
    roman = ""
    i = 0
    while num > 0:
        for _ in range(num // values[i]):
            roman += symbols[i]
            num -= values[i]
        i += 1
    return roman

def roman_to_int(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for c in s[::-1]:
        value = roman_map[c]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

integer1 = 3
integer2 = 4
integer3 = 9
integer4 = 58
integer5 = 1994

roman1 = "III"
roman2 = "IV"
roman3 = "IX"
roman4 = "LVIII"
roman5 = "MCMXCIV"

print(f"{integer1} in Roman numerals is: {int_to_roman(integer1)}")
print(f"{integer2} in Roman numerals is: {int_to_roman(integer2)}")
print(f"{integer3} in Roman numerals is: {int_to_roman(integer3)}")
print(f"{integer4} in Roman numerals is: {int_to_roman(integer4)}")
print(f"{integer5} in Roman numerals is: {int_to_roman(integer5)}")

print(f"{roman1} in integer is: {roman_to_int(roman1)}")
print(f"{roman2} in integer is: {roman_to_int(roman2)}")
print(f"{roman3} in integer is: {roman_to_int(roman3)}")
print(f"{roman4} in integer is: {roman_to_int(roman4)}")
print(f"{roman5} in integer is: {roman_to_int(roman5)}")