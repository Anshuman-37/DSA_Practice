# Question 29: Longest Common Substring problem (DP approach).
def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    result = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0
    return result


string1 = "fish"
string2 = "fosh"

lcs_length = longest_common_substring(string1, string2)
print(f"Length of Longest Common Substring: {lcs_length}")
