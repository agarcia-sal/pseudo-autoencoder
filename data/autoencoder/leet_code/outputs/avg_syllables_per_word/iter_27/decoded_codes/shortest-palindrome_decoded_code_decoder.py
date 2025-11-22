class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "":
            return s

        def is_palindrome(check_str: str) -> bool:
            reversed_str = ""
            for index in range(len(check_str) - 1, -1, -1):
                reversed_str += check_str[index]
            return check_str == reversed_str

        for i in range(len(s), -1, -1):
            prefix_substring = s[:i]
            if is_palindrome(prefix_substring):
                suffix_substring = s[i:]
                reversed_suffix = ""
                for index in range(len(suffix_substring) - 1, -1, -1):
                    reversed_suffix += suffix_substring[index]
                return reversed_suffix + s