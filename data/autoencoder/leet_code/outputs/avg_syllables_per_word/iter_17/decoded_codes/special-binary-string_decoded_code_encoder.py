class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def dfs(substring: str) -> str:
            count = 0
            start_position = 0
            specials_list = []

            for index, character in enumerate(substring):
                if character == '1':
                    count += 1
                else:
                    count -= 1

                if count == 0:
                    # Recursively process the inner substring and wrap it with '1' and '0'
                    specials_list.append('1' + dfs(substring[start_position + 1:index]) + '0')
                    start_position = index + 1

            # Sort all special substrings in descending lexicographical order and join them
            specials_list.sort(reverse=True)
            return ''.join(specials_list)

        return dfs(s)