class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(num: int) -> bool:
            s = str(num)
            return s == s[::-1]

        def generate_palindromes(limit: int) -> list[int]:
            palindromes = []
            for i in range(1, 100_000):
                s = str(i)
                # Odd-length palindrome
                pal_odd = int(s + s[-2::-1])
                # Even-length palindrome
                pal_even = int(s + s[::-1])
                if pal_odd <= limit:
                    palindromes.append(pal_odd)
                if pal_even <= limit:
                    palindromes.append(pal_even)
            return palindromes

        left_num = int(left)
        right_num = int(right)
        limit = int(right_num**0.5) + 1
        palindromes = generate_palindromes(limit)

        count = 0
        for p in palindromes:
            square = p * p
            if left_num <= square <= right_num and is_palindrome(square):
                count += 1

        return count