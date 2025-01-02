# Question 23: Shortest common superstring or shortest string containing two given
def shortest_common_superstring_dp(str1, str2):
    m = len(str1)
    n = len(str2)

    # Calculate LCS length using DP
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = m
    j = n
    superstring = ""
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            superstring += str1[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                superstring += str1[i - 1]
                i -= 1
            else:
                superstring += str2[j - 1]
                j -= 1

    while i > 0:
        superstring += str1[i - 1]
        i -= 1
    while j > 0:
        superstring += str2[j - 1]
        j -= 1

    return superstring[::-1]

string1 = "geek"
string2 = "eke"
string3 = "AGGTAB"
string4 = "GXTXAYB"

print(f"Shortest common superstring of '{string1}' and '{string2}' (DP): {shortest_common_superstring_dp(string1, string2)}")
print(f"Shortest common superstring of '{string3}' and '{string4}' (DP): {shortest_common_superstring_dp(string3, string4)}")