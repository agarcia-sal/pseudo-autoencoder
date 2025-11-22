class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        i2 = i3 = i5 = 0
        while len(ugly_numbers) < n:
            next2 = ugly_numbers[i2] * 2
            next3 = ugly_numbers[i3] * 3
            next5 = ugly_numbers[i5] * 5
            next_ugly = min(next2, next3, next5)
            ugly_numbers.append(next_ugly)
            if next_ugly == next2:
                i2 += 1
            if next_ugly == next3:
                i3 += 1
            if next_ugly == next5:
                i5 += 1
        return ugly_numbers[n-1]