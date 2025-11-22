from typing import List

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def generate_strobogrammatic(n: int, final_length: int) -> List[str]:
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]

            middles = generate_strobogrammatic(n - 2, final_length)
            result = []
            for middle in middles:
                if n != final_length:
                    # Avoid numbers with leading zero
                    result.append("0" + middle + "0")
                result.append("1" + middle + "1")
                result.append("6" + middle + "9")
                result.append("8" + middle + "8")
                result.append("9" + middle + "6")
            return result

        def count_strobogrammatic(low: str, high: str) -> int:
            count = 0
            len_low, len_high = len(low), len(high)
            for length in range(len_low, len_high + 1):
                candidates = generate_strobogrammatic(length, length)
                for num in candidates:
                    if (length == len_low and num < low) or (length == len_high and num > high):
                        continue
                    count += 1
            return count

        return count_strobogrammatic(low, high)