# Question 11: Convert a string to an integer (atoi).

def atoi_optimal(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    sign = 1
    index = 0
    if s[index] == '+':
        index += 1
    elif s[index] == '-':
        sign = -1
        index += 1
    result = 0
    while index < len(s) and s[index].isdigit():
        digit = ord(s[index]) - ord('0')
        if result > (2 ** 31 - 1) // 10 or (result == (2 ** 31 - 1) // 10 and digit > 7):
            return 2 ** 31 - 1 if sign == 1 else -2 ** 31
        if result < (-2 ** 31) // 10 or (result == (-2 ** 31) // 10 and digit > 8):
            return -2 ** 31 if sign == -1 else 2 ** 31 - 1

        result = result * 10 + digit
        index += 1
    return result * sign


print(atoi_optimal("   -42"))
print(atoi_optimal("4193 with words"))
print(atoi_optimal("words and 987"))
print(atoi_optimal("-91283472332"))
