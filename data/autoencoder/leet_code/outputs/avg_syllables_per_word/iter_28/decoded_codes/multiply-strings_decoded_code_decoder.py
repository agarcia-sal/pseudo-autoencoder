from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result: List[int] = [0] * (len(num1) + len(num2))

        num1_rev = num1[::-1]
        num2_rev = num2[::-1]

        for i in range(len(num1_rev)):
            digit1 = ord(num1_rev[i]) - ord('0')
            for j in range(len(num2_rev)):
                digit2 = ord(num2_rev[j]) - ord('0')
                mul = digit1 * digit2
                p1 = i + j
                p2 = i + j + 1
                sum_ = mul + result[p1]

                result[p1] = sum_ % 10
                result[p2] += sum_ // 10

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result_str = ''.join(str(d) for d in reversed(result))
        return result_str