from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                email_to_name[email] = name
            first_email = emails[0]
            for email in emails[1:]:
                graph[first_email].add(email)
                graph[email].add(first_email)
        seen = set()
        merged_accounts = []

        def dfs(email, component):
            seen.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in seen:
                    dfs(neighbor, component)

        # For every email in the mapping, if not seen, perform DFS.
        for email in email_to_name:
            if email not in seen:
                component = []
                dfs(email, component)
                # Sort emails lexicographically.
                component.sort()
                # Prepend the name.
                merged_accounts.append([email_to_name[email]] + component)

        return merged_accounts
