class Solution:
    def partition(self, s):
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path)
                return
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if is_palindrome(substr):
                    backtrack(end, path + [substr])

        result = []
        backtrack(0, [])
        return result