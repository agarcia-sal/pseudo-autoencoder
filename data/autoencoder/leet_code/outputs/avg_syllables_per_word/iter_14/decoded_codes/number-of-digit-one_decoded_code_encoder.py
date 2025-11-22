class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        count = 0
        factor = 1

        while factor <= n:
            lower_nums = n - (n // factor) * factor
            cur_num = (n // factor) % 10
            higher_nums = n // (factor * 10)

            if cur_num == 0:
                count += higher_nums * factor
            elif cur_num == 1:
                count += higher_nums * factor + lower_nums + 1
            else:
                count += (higher_nums + 1) * factor

            factor *= 10

        return count