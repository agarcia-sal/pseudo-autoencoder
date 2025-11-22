class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        def dfs(u: int) -> list[str]:
            if u == 0:
                return [""]
            if u == 1:
                return ["0", "1", "8"]
            ans = []
            for v in dfs(u - 2):
                for pair in ["11", "88", "69", "96"]:
                    ans.append(pair[0] + v + pair[1])
                if u != n:
                    ans.append("0" + v + "0")
            return ans
        return dfs(n)