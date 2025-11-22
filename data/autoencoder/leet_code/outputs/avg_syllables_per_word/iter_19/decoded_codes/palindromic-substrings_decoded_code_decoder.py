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
        for index in range(len(s)):
            total_palindromes += expand_around_center(index, index)
            total_palindromes += expand_around_center(index, index + 1)
        return total_palindromes