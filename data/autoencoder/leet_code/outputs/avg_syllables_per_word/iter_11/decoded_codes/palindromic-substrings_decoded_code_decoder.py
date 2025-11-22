class Solution:
    def countSubstrings(self, s):
        def expand_around_center(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total_palindromes = 0
        for i in range(len(s)):
            total_palindromes += expand_around_center(i, i)
            total_palindromes += expand_around_center(i, i + 1)
        return total_palindromes