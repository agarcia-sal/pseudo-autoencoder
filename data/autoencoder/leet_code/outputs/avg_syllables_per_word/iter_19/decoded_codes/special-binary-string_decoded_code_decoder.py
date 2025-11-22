class Solution:
    def makeLargestSpecial(self, s):
        def dfs(s):
            count = 0
            start = 0
            specials = []
            for i, ch in enumerate(s):
                if ch == '1':
                    count += 1
                else:
                    count -= 1
                if count == 0:
                    # recursively process the inner substring excluding the outer '1' and '0'
                    specials.append('1' + dfs(s[start + 1:i]) + '0')
                    start = i + 1
            specials.sort(reverse=True)
            return ''.join(specials)
        return dfs(s)