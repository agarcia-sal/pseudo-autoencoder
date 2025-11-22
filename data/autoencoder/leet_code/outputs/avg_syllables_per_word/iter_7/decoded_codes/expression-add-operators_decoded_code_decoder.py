from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(index: int, path: str, value: int, prev: int) -> None:
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for i in range(index + 1, len(num) + 1):
                operand = num[index:i]
                if len(operand) > 1 and operand[0] == '0':
                    continue

                cur = int(operand)
                if index == 0:
                    dfs(i, operand, cur, cur)
                else:
                    dfs(i, path + '+' + operand, value + cur, cur)
                    dfs(i, path + '-' + operand, value - cur, -cur)
                    dfs(i, path + '*' + operand, value - prev + prev * cur, prev * cur)

        result: List[str] = []
        dfs(0, '', 0, 0)
        return result