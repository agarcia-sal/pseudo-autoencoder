class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def generate_strobogrammatic(n: int, final_length: int) -> list[str]:
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]

            middles = generate_strobogrammatic(n - 2, final_length)
            result = []
            for middle in middles:
                if n != final_length:
                    result.append("0" + middle + "0")
                result.append("1" + middle + "1")
                result.append("6" + middle + "9")
                result.append("8" + middle + "8")
                result.append("9" + middle + "6")
            return result

        def count_strobogrammatic(low: str, high: str) -> int:
            count = 0
            low_len = len(low)
            high_len = len(high)
            for length in range(low_len, high_len + 1):
                for num in generate_strobogrammatic(length, length):
                    # Skip numbers with leading zero unless single digit
                    if length > 1 and num[0] == '0':
                        continue
                    if length == low_len and num < low:
                        continue
                    if length == high_len and num > high:
                        continue
                    count += 1
            return count

        return count_strobogrammatic(low, high)