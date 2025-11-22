from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def dfs(u: int) -> List[str]:
            if u == 0:
                return [""]
            if u == 1:
                return ["0", "1", "8"]
            ans = []
            for v in dfs(u - 2):
                for pair in ["11", "88", "69", "96"]:
                    l, r = pair[0], pair[1]
                    ans.append(l + v + r)
                if u != n:
                    ans.append("0" + v + "0")
            return ans
        return dfs(n)