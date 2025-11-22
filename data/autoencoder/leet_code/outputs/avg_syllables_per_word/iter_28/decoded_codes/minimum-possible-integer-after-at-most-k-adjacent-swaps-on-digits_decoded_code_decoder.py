from typing import List

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        num = list(num)
        n = len(num)

        while k > 0:
            swapped = False
            for i in range(n - 1):
                if num[i] > num[i + 1]:
                    min_digit = '9'
                    min_index = -1
                    end = min(i + k + 1, n)
                    for j in range(i, end):
                        if num[j] < min_digit:
                            min_digit = num[j]
                            min_index = j
                    # Move num[min_index] to position i by shifting intermediate elements right
                    digit = num[min_index]
                    for j in range(min_index, i, -1):
                        num[j] = num[j - 1]
                    num[i] = digit
                    k -= (min_index - i)
                    swapped = True
                    break
            if not swapped:
                break

        return ''.join(num)