class Solution:
    def primePalindrome(self, n):
        def is_prime(num):
            if num < 2:
                return False
            if num == 2 or num == 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        def is_palindrome(num):
            s = str(num)
            return s == s[::-1]

        if n <= 2:
            return 2

        if 10 <= n <= 11:
            return 11

        while True:
            if n % 2 == 0:
                n += 1
                continue
            if is_palindrome(n) and is_prime(n):
                return n
            if len(str(n)) % 2 == 0:
                n = 10 ** (len(str(n)) + 1)
            else:
                n += 2