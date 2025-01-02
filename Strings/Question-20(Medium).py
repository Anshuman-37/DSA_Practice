# Question 20: Longest Repeating Substring
def longest_repeating_substring_dp(s):
    n = len(s)
    if n < 2:
        return ""

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    longest_substring = ""
    max_length = 0

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if s[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    longest_substring = s[i - max_length:i]

    return longest_substring

string1 = "banana"
string2 = "abcd"
string3 = "aabcaabdaab"

print(f"Longest repeating substring of '{string1}' (DP): {longest_repeating_substring_dp(string1)}")

print(f"Longest repeating substring of '{string2}' (DP): {longest_repeating_substring_dp(string2)}")

print(f"Longest repeating substring of '{string3}' (DP): {longest_repeating_substring_dp(string3)}")

