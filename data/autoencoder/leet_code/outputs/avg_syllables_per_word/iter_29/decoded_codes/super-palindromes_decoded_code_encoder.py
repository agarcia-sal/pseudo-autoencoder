class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(number: int) -> bool:
            s = str(number)
            return s == s[::-1]

        def generate_palindromes(limit: int) -> list[int]:
            palindromes_list = []
            for integer_value in range(1, 100000):
                s = str(integer_value)
                # Odd length palindrome: append s + reversed(s[:-1])
                odd_pal = int(s + s[-2::-1])
                # Even length palindrome: append s + reversed(s)
                even_pal = int(s + s[::-1])
                palindromes_list.append(odd_pal)
                palindromes_list.append(even_pal)
            return [p for p in palindromes_list if p <= limit]

        left_int = int(left)
        right_int = int(right)
        limit = int(right_int**0.5) + 1
        palindromes = generate_palindromes(limit)

        count = 0
        for palindrome_value in palindromes:
            square = palindrome_value * palindrome_value
            if left_int <= square <= right_int and is_palindrome(square):
                count += 1
        return count