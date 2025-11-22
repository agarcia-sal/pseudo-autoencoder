class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                sum_ = mul + result[p1]

                result[p1] = sum_ % 10
                result[p2] += sum_ // 10

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return ''.join(map(str, result[::-1]))