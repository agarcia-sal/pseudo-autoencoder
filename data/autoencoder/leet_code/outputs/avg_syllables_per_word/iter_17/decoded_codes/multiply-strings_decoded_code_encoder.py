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

        return self.convert_result_array_to_string(result_list)

    def convert_result_array_to_string(self, result_list) -> str:
        reversed_list = result_list[::-1]
        result_string = ''.join(str(d) for d in reversed_list)
        stripped_string = result_string.lstrip('0')
        return stripped_string if stripped_string else "0"