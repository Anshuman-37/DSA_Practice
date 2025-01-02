# Question 30: Word Break problem (segment a string into dictionary words).
def word_break_dp(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]

s = "applepenapple"
word_dict = {"apple", "pen"}

print(f"Can '{s}' be segmented (DP)? {word_break_dp(s, word_dict)}")