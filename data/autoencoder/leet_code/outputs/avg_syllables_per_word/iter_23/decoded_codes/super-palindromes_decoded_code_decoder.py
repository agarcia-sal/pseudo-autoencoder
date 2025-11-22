import math

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(num: int) -> bool:
            s = str(num)
            return s == s[::-1]

        def generate_palindromes(limit: int) -> list[int]:
            palindromes = []
            for i in range(1, 100_000):
                s = str(i)
                # odd length palindrome: s + s[-2::-1]
                odd_palindrome_str = s + s[-2::-1]
                odd_palindrome = int(odd_palindrome_str)
                palindromes.append(odd_palindrome)

                # even length palindrome: s + s[::-1]
                even_palindrome_str = s + s[::-1]
                even_palindrome = int(even_palindrome_str)
                palindromes.append(even_palindrome)

            filtered_palindromes = [p for p in palindromes if p <= limit]
            return filtered_palindromes

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