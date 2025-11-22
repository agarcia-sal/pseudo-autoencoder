class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1
                sum_ = mul + result[p1]
                result[p1] = sum_ % 10
                result[p2] += sum_ // 10

        # Remove leading zeros from the tail end of the reversed result
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result_str = ''.join(str(d) for d in reversed(result))
        return result_str