import math

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(num: int) -> bool:
            num_str = str(num)
            return num_str == num_str[::-1]

        def generate_palindromes(limit: int) -> list[int]:
            palindromes = []
            for i in range(1, 100000):
                s = str(i)
                # odd-length palindrome: s + reverse(s[:-1])
                odd_pal = int(s + s[-2::-1])
                palindromes.append(odd_pal)
                # even-length palindrome: s + reverse(s)
                even_pal = int(s + s[::-1])
                palindromes.append(even_pal)
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