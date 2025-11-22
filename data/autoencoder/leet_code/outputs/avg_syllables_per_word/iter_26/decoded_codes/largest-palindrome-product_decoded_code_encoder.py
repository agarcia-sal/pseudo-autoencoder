class Solution:
    def largestPalindrome(self, number_n: int) -> int:
        if number_n == 1:
            return 9

        upper_limit = 10 ** number_n - 1
        lower_limit = 10 ** (number_n - 1)

        max_palindrome = 0

        for number_i in range(upper_limit, lower_limit - 1, -1):
            for number_j in range(number_i, lower_limit - 1, -1):
                product = number_i * number_j
                if product <= max_palindrome:
                    break
                str_product = str(product)
                if str_product == str_product[::-1]:
                    max_palindrome = product

        return max_palindrome % 1337