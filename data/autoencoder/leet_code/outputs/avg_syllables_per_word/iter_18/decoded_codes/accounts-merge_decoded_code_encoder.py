from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, size: int):
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])  # path compression
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id = {}
        uf = UnionFind(len(accounts))

        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email not in email_to_id:
                    email_to_id[email] = i
                else:
                    uf.union(i, email_to_id[email])

        merged_emails = defaultdict(list)
        for email, account_id in email_to_id.items():
            root_id = uf.find(account_id)
            merged_emails[root_id].append(email)

        result = []
        for account_id, emails in merged_emails.items():
            name = accounts[account_id][0]
            result.append([name] + sorted(emails))

        return result