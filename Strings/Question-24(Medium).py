# Question 24: Edit Distance between two strings.
def edit_distance_dp(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            # If first string is empty, only option is to insert all characters of second string
            if i == 0:
                dp[i][j] = j
            # If second string is empty, only option is to remove all characters of first string
            elif j == 0:
                dp[i][j] = i
            # If last characters are same, ignore them and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # If last character are different, consider all possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]

str1 = "sunday"
str2 = "saturday"

print(f"Edit distance (DP): {edit_distance_dp(str1, str2)}")