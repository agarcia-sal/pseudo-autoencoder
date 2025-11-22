class Solution:
    def primePalindrome(self, number_n: int) -> int:
        def is_prime(number_num: int) -> bool:
            if number_num < 2:
                return False
            if number_num == 2 or number_num == 3:
                return True
            if number_num % 2 == 0 or number_num % 3 == 0:
                return False
            i = 5
            while i * i <= number_num:
                if number_num % i == 0 or number_num % (i + 2) == 0:
                    return False
                i += 6
            return True

        def is_palindrome(number_num: int) -> bool:
            s = str(number_num)
            return s == s[::-1]

        if number_n <= 2:
            return 2
        if 10 <= number_n <= 11:
            return 11

        while True:
            if number_n % 2 == 0:
                number_n += 1
                continue
            if is_palindrome(number_n) and is_prime(number_n):
                return number_n
            s_len = len(str(number_n))
            if s_len % 2 == 0:
                number_n = 10 ** (s_len + 1)
            else:
                number_n += 2