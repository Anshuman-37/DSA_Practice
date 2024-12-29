# Question 17: Find the longest common prefix among a set of strings
def longest_common_prefix_divide_conquer(strs):
    if not strs:
        return ""

    def common_prefix(str1, str2):
        min_len = min(len(str1), len(str2))
        for i in range(min_len):
            if str1[i] != str2[i]:
                return str1[:i]
        return str1[:min_len]

    def lcp(low, high):
        if low == high:
            return strs[low]
        mid = (low + high) // 2
        lcp_left = lcp(low, mid)
        lcp_right = lcp(mid + 1, high)
        return common_prefix(lcp_left, lcp_right)

    return lcp(0, len(strs) - 1)

strs = ["flower", "flow", "flight"]

print(f"Divide and Conquer: {longest_common_prefix_divide_conquer(strs)}")

strs = ["dog", "racecar", "car"]

print(f"Divide and Conquer: {longest_common_prefix_divide_conquer(strs)}")