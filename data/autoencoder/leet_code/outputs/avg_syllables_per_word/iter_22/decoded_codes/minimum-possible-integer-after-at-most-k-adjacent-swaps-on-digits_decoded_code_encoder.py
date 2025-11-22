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
                    # Find the minimum digit within the allowed swap range
                    for j in range(i, end):
                        if num[j] < min_digit:
                            min_digit = num[j]
                            min_index = j
                    # Rotate: bring the min_digit to position i
                    if min_index != -1:
                        # Move element at min_index to i, shift others right by one
                        min_char = num.pop(min_index)
                        num.insert(i, min_char)
                        k -= (min_index - i)
                        swapped = True
                        break
            if not swapped:
                break

        return "".join(num)