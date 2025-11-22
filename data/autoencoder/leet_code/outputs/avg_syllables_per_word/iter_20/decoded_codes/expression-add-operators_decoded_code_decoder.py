class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        def dfs(index: int, path: str, value: int, prev: int):
            if index == len(num):
                if value == target:
                    result.append(path)
                return
            for i in range(index + 1, len(num) + 1):
                operand = num[index:i]
                if len(operand) > 1 and operand[0] == '0':
                    continue
                val = int(operand)
                if index == 0:
                    dfs(i, operand, val, val)
                else:
                    dfs(i, path + '+' + operand, value + val, val)
                    dfs(i, path + '-' + operand, value - val, -val)
                    dfs(i, path + '*' + operand, value - prev + prev * val, prev * val)

        result = []
        dfs(0, '', 0, 0)
        return result