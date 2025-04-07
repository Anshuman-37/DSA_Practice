from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        groups = []
        i = 0
        # Parse the string into groups
        while i < len(s):
            if s[i] == '{':
                i += 1  # skip '{'
                options = []
                # Collect all options until we reach '}'
                while s[i] != '}':
                    if s[i] != ',':
                        options.append(s[i])
                    i += 1
                groups.append(sorted(options))  # sort to help with lexicographical order
                i += 1  # skip '}'
            else:
                groups.append([s[i]])
                i += 1

        result = []

        # Backtracking helper function
        def backtrack(idx, path):
            if idx == len(groups):
                result.append("".join(path))
                return
            for char in groups[idx]:
                path.append(char)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])
        return sorted(result)
