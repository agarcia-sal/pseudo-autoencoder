class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(number: int) -> bool:
            s = str(number)
            return s == s[::-1]

        def generate_palindromes(limit: int):
            res = []
            for i in range(1, 100_000):
                s = str(i)
                # Odd-length palindrome
                res.append(int(s + s[-2::-1]))
                # Even-length palindrome
                res.append(int(s + s[::-1]))
            return [p for p in res if p <= limit]

        left_int = int(left)
        right_int = int(right)
        limit = int(right_int ** 0.5) + 1
        palindromes = generate_palindromes(limit)

        count = 0
        for p in palindromes:
            square = p * p
            if left_int <= square <= right_int and is_palindrome(square):
                count += 1

        return count