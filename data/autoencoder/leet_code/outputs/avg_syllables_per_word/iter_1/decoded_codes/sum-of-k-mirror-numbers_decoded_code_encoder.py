def is_palindrome(s):
    return s == s[::-1]

def to_base_k(num, k):
    if num == 0:
        return "0"
    digits = []
    while num > 0:
        digits.append(str(num % k))
        num = num // k
    return "".join(digits[::-1])

def generate_palindromes(length):
    if length == 1:
        for i in range(1, 10):
            yield str(i)
    else:
        start = 10 ** ((length - 1) // 2)
        end = 10 ** ((length + 1) // 2)
        for half in range(start, end):
            half_str = str(half)
            if length % 2 == 0:
                pal = half_str + half_str[::-1]
            else:
                pal = half_str + half_str[-2::-1]
            yield pal

def kMirror(k, n):
    res = []
    length = 1
    while len(res) < n:
        for p in generate_palindromes(length):
            num = int(p)
            if is_palindrome(to_base_k(num, k)):
                res.append(num)
                if len(res) == n:
                    break
        length += 1
    return sum(res)