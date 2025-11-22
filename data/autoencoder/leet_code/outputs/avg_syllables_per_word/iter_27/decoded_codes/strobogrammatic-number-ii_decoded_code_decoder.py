from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def dfs(u: int) -> List[str]:
            if u == 0:
                return [""]
            if u == 1:
                return ["0", "1", "8"]
            ans = []
            pairs = [("1", "1"), ("8", "8"), ("6", "9"), ("9", "6")]
            for v in dfs(u - 2):
                for l, r in pairs:
                    ans.append(l + v + r)
                if u != n:
                    ans.append("0" + v + "0")
            return ans
        return dfs(n)