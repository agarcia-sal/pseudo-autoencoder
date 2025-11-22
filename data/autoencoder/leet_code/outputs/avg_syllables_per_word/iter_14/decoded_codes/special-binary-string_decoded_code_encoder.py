class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def dfs(s: str) -> str:
            count = 0
            start = 0
            specials = []
            for i, char in enumerate(s):
                count += 1 if char == '1' else -1
                if count == 0:
                    # Recursively make the inner substring largest special
                    specials.append('1' + dfs(s[start + 1:i]) + '0')
                    start = i + 1
            specials.sort(reverse=True)
            return ''.join(specials)

        return dfs(s)