class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        pairs = [("1", "1"), ("8", "8"), ("6", "9"), ("9", "6")]

        def dfs(u: int) -> list[str]:
            if u == 0:
                return [""]
            if u == 1:
                return ["0", "1", "8"]
            result = []
            for val in dfs(u - 2):
                for left, right in pairs:
                    result.append(left + val + right)
                if u != n:
                    result.append("0" + val + "0")
            return result

        return dfs(n)