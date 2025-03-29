class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Use dp[i] to record to number of good strings of length i.
        dp = [1] + [0] * (high)
        mod = 10 ** 9 + 7
        for end in range(1, high+1):
            # Check if the current string can be made by appending zero 0s or one 1's
            if end >= zero:
                dp[end] += dp[end-zero]
            if end >= one:
                dp[end] += dp[end-one]
            dp[end] %= mod
        # ADd the number of strings with each valid length [low ~ high]
        return sum(dp[low:high+1]) % mod

def something():
    str1 = str1.lower().split("")
    str2 = str2.lower().split("")

    len_str1 = len(str1)
    len_str2 = len(str2)

    # Base Case
    if not str1 and not str2:
        return False

    i, j = 0, 0

    if len_str1 > len_str2:
        str1, str2 = str2, str1

    while str1[i] and str2[j]:
        if str1[i] == str2[j]:
            i += 1
            j += 1
        if str1[i] != str2[j]:
            j += 1

    if i == j:
        return True

    if i != len_str1:
        return False

    return abs(len_str1 - len_str2) > 2

str1 = " She is amazing"
print(str1.lower().split(" "))