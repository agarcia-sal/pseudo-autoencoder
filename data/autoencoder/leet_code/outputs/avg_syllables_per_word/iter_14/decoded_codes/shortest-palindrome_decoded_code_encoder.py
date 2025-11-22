class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "":
            return s

        def is_palindrome(check_str: str) -> bool:
            return check_str == check_str[::-1]

        for i in range(len(s), -1, -1):
            substring_to_check = s[:i]
            if is_palindrome(substring_to_check):
                to_add = s[i:][::-1]
                return to_add + s