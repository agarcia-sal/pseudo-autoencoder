import math

class Solution:
    def superpalindromesInRange(self, left, right):
        def is_palindrome(num):
            s = str(num)
            return s == s[::-1]

        def generate_palindromes(limit):
            palindromes = []
            for i in range(1, 100000):
                s = str(i)
                # Odd-length palindrome
                pal1 = int(s + s[-2::-1])
                # Even-length palindrome
                pal2 = int(s + s[::-1])
                palindromes.append(pal1)
                palindromes.append(pal2)
            return [p for p in palindromes if p <= limit]

        left = int(left)
        right = int(right)
        limit = int(math.isqrt(right)) + 1
        palindromes = generate_palindromes(limit)

        count = 0
        for p in palindromes:
            square = p * p
            if left <= square <= right and is_palindrome(square):
                count += 1

        return count