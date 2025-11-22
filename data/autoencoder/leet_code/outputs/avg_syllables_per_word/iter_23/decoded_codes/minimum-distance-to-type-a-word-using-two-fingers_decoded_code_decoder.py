class Solution:
    def minimumDistance(self, word: str) -> int:
        def distance(c1, c2) -> int:
            if c1 is None:
                return 0
            x1 = (ord(c1) - ord('A')) // 6
            y1 = (ord(c1) - ord('A')) % 6
            x2 = (ord(c2) - ord('A')) // 6
            y2 = (ord(c2) - ord('A')) % 6
            return abs(x1 - x2) + abs(y1 - y2)

        memo = {}

        def dp(i, f1, f2) -> int:
            if i == len(word):
                return 0
            key = (i, f1, f2)
            if key in memo:
                return memo[key]
            c = word[i]
            d1 = distance(f1, c) + dp(i + 1, c, f2)
            d2 = distance(f2, c) + dp(i + 1, f1, c)
            memo[key] = min(d1, d2)
            return memo[key]

        return dp(0, None, None)