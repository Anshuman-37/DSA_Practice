# Question 19: Longest Palindromic Substring.
def longest_palindrome_dp(s):
    n = len(s)
    if n < 2:
        return s
    dp = [[False] * n for _ in range(n)]
    longest_palindrome = s[0]

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            longest_palindrome = s[i:i + 2]

    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                longest_palindrome = s[i:j + 1]

    return longest_palindrome

string1 = "babad"
string2 = "cbbd"
string3 = "a"
string4 = ""

print(f"Longest palindromic substring of '{string1}' (DP): {longest_palindrome_dp(string1)}")

print(f"Longest palindromic substring of '{string2}' (DP): {longest_palindrome_dp(string2)}")

print(f"Longest palindromic substring of '{string3}' (DP): {longest_palindrome_dp(string3)}")

print(f"Longest palindromic substring of '{string4}' (DP): {longest_palindrome_dp(string4)}")