class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(num: int) -> bool:
            s = str(num)
            return s == s[::-1]

        def generate_palindromes(limit: int):
            palindromes = []
            for i in range(1, 100000):
                s = str(i)
                pal1 = int(s + s[-2::-1])  # odd length palindrome
                pal2 = int(s + s[::-1])    # even length palindrome
                if pal1 <= limit:
                    palindromes.append(pal1)
                if pal2 <= limit:
                    palindromes.append(pal2)
            return palindromes

        left_int, right_int = int(left), int(right)
        limit = int(right_int**0.5) + 1
        palindromes = generate_palindromes(limit)
        count = 0
        for p in palindromes:
            square = p * p
            if left_int <= square <= right_int and is_palindrome(square):
                count += 1
        return count