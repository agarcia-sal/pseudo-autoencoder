class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result_list = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1
                sum_value = mul + result_list[p1]

                result_list[p1] = sum_value % 10
                result_list[p2] += sum_value // 10

        # Remove leading zeros from the reversed result string
        reversed_result_string = "".join(str(d) for d in reversed(result_list)).lstrip('0')
        return reversed_result_string if reversed_result_string else "0"