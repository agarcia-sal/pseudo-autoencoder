from math import sqrt

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(num: int) -> bool:
            s = str(num)
            return s == s[::-1]

        def generate_palindromes(limit: int) -> list[int]:
            palindromes = []
            for i in range(1, 100_000):
                s = str(i)
                # odd length palindrome
                odd_pal = int(s + s[-2::-1])
                # even length palindrome
                even_pal = int(s + s[::-1])
                if odd_pal <= limit:
                    palindromes.append(odd_pal)
                if even_pal <= limit:
                    palindromes.append(even_pal)
            return palindromes

        left_int = int(left)
        right_int = int(right)
        limit = int(sqrt(right_int)) + 1
        palindromes = generate_palindromes(limit)

        count = 0
        for p in palindromes:
            square = p * p
            if left_int <= square <= right_int and is_palindrome(square):
                count += 1

        return count