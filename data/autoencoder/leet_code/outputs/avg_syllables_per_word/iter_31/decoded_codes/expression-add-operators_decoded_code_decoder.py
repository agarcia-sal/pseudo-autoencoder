from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def dfs(index: int, path: str, value: int, prev: int) -> None:
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for i in range(index + 1, len(num) + 1):
                operand_str = num[index:i]
                if len(operand_str) > 1 and operand_str[0] == '0':
                    continue
                operand = int(operand_str)

                if index == 0:
                    dfs(i, operand_str, operand, operand)
                else:
                    dfs(i, path + '+' + operand_str, value + operand, operand)
                    dfs(i, path + '-' + operand_str, value - operand, -operand)
                    dfs(i, path + '*' + operand_str, value - prev + prev * operand, prev * operand)

        dfs(0, '', 0, 0)
        return result