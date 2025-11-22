class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        upper_limit = 10**n - 1
        lower_limit = 10**(n - 1)
        max_palindrome = 0

        for i in range(upper_limit, lower_limit - 1, -1):
            if i * upper_limit <= max_palindrome:
                break
            for j in range(i, lower_limit - 1, -1):
                product = i * j
                if product <= max_palindrome:
                    break
                s = str(product)
                if s == s[::-1]:
                    max_palindrome = product

        return max_palindrome % 1337