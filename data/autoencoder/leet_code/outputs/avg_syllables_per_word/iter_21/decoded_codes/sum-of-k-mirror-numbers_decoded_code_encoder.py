class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def to_base_k(num: int, k: int) -> str:
            if num == 0:
                return "0"
            digits = []
            while num > 0:
                digits.append(str(num % k))
                num //= k
            return "".join(reversed(digits))

        def generate_palindromes(length: int):
            if length == 1:
                for i in range(1, 10):
                    yield str(i)
            else:
                start = 10 ** ((length - 1) // 2)
                end = 10 ** ((length + 1) // 2)
                for half in range(start, end):
                    half_str = str(half)
                    if length % 2 == 0:
                        full = half_str + half_str[::-1]
                    else:
                        full = half_str + half_str[-2::-1]
                    yield full

        k_mirror_numbers = []
        length = 1
        while len(k_mirror_numbers) < n:
            for pal in generate_palindromes(length):
                num = int(pal)
                if is_palindrome(to_base_k(num, k)):
                    k_mirror_numbers.append(num)
                    if len(k_mirror_numbers) == n:
                        break
            length += 1

        return sum(k_mirror_numbers)