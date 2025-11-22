def digitsCount(d, low, high):
    def count_digit(n, digit):
        cnt, p10, cur = 0, 1, n
        while cur > 0:
            last = cur % 10
            cur //= 10
            fc = cur - (1 if digit == 0 else 0)
            cnt += fc * p10
            if last > digit:
                cnt += p10
            elif last == digit:
                cnt += n % p10 + 1
            p10 *= 10
        return cnt

    return count_digit(high, d) - count_digit(low - 1, d)