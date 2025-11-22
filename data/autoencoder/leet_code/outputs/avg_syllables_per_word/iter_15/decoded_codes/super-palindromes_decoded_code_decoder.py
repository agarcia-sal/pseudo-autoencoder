import math

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(num: int) -> bool:
            s = str(num)
            return s == s[::-1]

        def generate_palindromes(limit: int) -> list[int]:
            palindromes = []
            for i in range(1, 100000):
                s = str(i)
                # Odd length palindrome
                pal_odd = int(s + s[-2::-1])
                # Even length palindrome
                pal_even = int(s + s[::-1])
                palindromes.append(pal_odd)
                palindromes.append(pal_even)
            return [p for p in palindromes if p <= limit]

        left_int = int(left)
        right_int = int(right)
        limit = int(math.isqrt(right_int)) + 1
        palindromes = generate_palindromes(limit)

        count = 0
        for p in palindromes:
            square = p * p
            if left_int <= square <= right_int and is_palindrome(square):
                count += 1

        return count