class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def dfs(special_string: str) -> str:
            count = 0
            start = 0
            specials = []

            for i, char in enumerate(special_string):
                if char == '1':
                    count += 1
                else:
                    count -= 1

                if count == 0:
                    # Recursively process the inner substring excluding the leading '1' and trailing '0'
                    specials.append('1' + dfs(special_string[start + 1:i]) + '0')
                    start = i + 1

            specials.sort(reverse=True)
            return ''.join(specials)

        return dfs(s)