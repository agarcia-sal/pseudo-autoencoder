class Solution:
    def strobogrammaticInRange(self, low, high):
        def generate_strobogrammatic(n, final_length):
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

        def count_strobogrammatic(low, high):
            count = 0
            len_low = len(low)
            len_high = len(high)
            for length in range(len_low, len_high + 1):
                for num in generate_strobogrammatic(length, length):
                    if (length == len_low and num < low) or (length == len_high and num > high):
                        continue
                    if length > 1 and num[0] == '0':
                        continue
                    count += 1
            return count

        return count_strobogrammatic(low, high)