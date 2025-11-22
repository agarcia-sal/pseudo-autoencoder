class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            sorted_list = sorted(s)
            result = "".join(sorted_list)
            return result
        else:
            n = len(s)
            smallest = s
            for i in range(1, n):
                rotated = s[i:] + s[:i]
                if rotated < smallest:
                    smallest = rotated
            return smallest