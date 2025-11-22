class Solution:
    def kMirror(self, k, n):
        def is_palindrome(s):
            return s == s[::-1]

        def to_base_k(num, k):
            if num == 0:
                return "0"
            digits = []
            while num > 0:
                digits.append(str(num % k))
                num //= k
            return ''.join(digits[::-1])

        def generate_palindromes(length):
            if length == 1:
                for i in range(1, 10):
                    yield str(i)
            else:
                half_len = length // 2
                start = 10 ** (half_len - 1 if length % 2 == 0 else half_len)
                end = 10 ** half_len
                # For even length palindrome, half length digits are mirrored entirely
                # For odd length palindrome, half_len digits plus middle digit plus reverse of half_len-1 digits
                # Pseudocode uses indexing from end 3 to 1 for odd length reverse substring
                # That corresponds to slicing off last character from half_str for the reverse part
                # After careful analysis, the pseudocode builds palindrome as:
                # if length even:
                #   full = half_str + reverse(half_str)
                # else:
                #   full = half_str + reverse(half_str[:-1])
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