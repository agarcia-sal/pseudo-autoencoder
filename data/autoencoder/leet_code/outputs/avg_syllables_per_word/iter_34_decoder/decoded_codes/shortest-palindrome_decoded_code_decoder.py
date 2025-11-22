class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s is None:
            return s

        def is_palindrome(check_str: str) -> bool:
            return check_str == check_str[::-1]

        for i in range(len(s), -1, -1):
            if is_palindrome(s[:i]):
                to_add = s[i:][::-1]
                return to_add + s