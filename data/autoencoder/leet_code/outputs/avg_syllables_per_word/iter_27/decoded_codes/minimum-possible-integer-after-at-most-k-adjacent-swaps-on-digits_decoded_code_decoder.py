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
                    upper_bound = min(i + k + 1, n)
                    for j in range(i, upper_bound):
                        if num[j] < min_digit:
                            min_digit = num[j]
                            min_index = j

                    # Reorder the segment: put min_digit at i, and shift others right
                    # That is: num[i:min_index+1] = [num[min_index]] + num[i:min_index]
                    new_segment = [num[min_index]] + num[i:min_index]
                    num[i:min_index+1] = new_segment

                    k -= (min_index - i)
                    swapped = True
                    break

            if not swapped:
                break

        return ''.join(num)