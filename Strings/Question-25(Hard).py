# Question 25: Wildcard pattern matching with '?' and '*'.
def is_match_dp_top_down(s, p):
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            if j == len(p):
                ans = i == len(s)
            else:
                first_match = i < len(s) and (p[j] == s[i] or p[j] == '?')
                if j + 1 < len(p) and p[j + 1] == '*':
                    ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                else:
                    ans = first_match and dp(i + 1, j + 1)
            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)

string1 = "aa"
pattern1 = "a"
string2 = "aa"
pattern2 = "*"
string3 = "cb"
pattern3 = "?a"
string4 = "adceb"
pattern4 = "*a*b"
string5 = "acdcb"
pattern5 = "a*c?b"

print(f"'{string1}' matches '{pattern1}' (DP Top-Down): {is_match_dp_top_down(string1, pattern1)}")

print(f"'{string2}' matches '{pattern2}' (DP Top-Down): {is_match_dp_top_down(string2, pattern2)}")

print(f"'{string3}' matches '{pattern3}' (DP Top-Down): {is_match_dp_top_down(string3, pattern3)}")

print(f"'{string4}' matches '{pattern4}' (DP Top-Down): {is_match_dp_top_down(string4, pattern4)}")

print(f"'{string5}' matches '{pattern5}' (DP Top-Down): {is_match_dp_top_down(string5, pattern5)}")
