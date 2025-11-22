from typing import List

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def dfs(s: str) -> str:
            count = 0
            start = 0
            specials: List[str] = []
            for i, char in enumerate(s):
                if char == '1':
                    count += 1
                else:
                    count -= 1
                if count == 0:
                    specials.append('1' + dfs(s[start + 1:i]) + '0')
                    start = i + 1
            specials.sort(reverse=True)
            return ''.join(specials)

        return dfs(s)