class Solution:
    def addOperators(self, num: str, target: int):
        result = []

        def dfs(index, path, value, prev):
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for i in range(index + 1, len(num) + 1):
                operand = num[index:i]
                if len(operand) > 1 and operand[0] == '0':
                    continue
                curr = int(operand)

                if index == 0:
                    dfs(i, operand, curr, curr)
                else:
                    dfs(i, path + "+" + operand, value + curr, curr)
                    dfs(i, path + "-" + operand, value - curr, -curr)
                    dfs(i, path + "*" + operand, value - prev + prev * curr, prev * curr)

        dfs(0, "", 0, 0)
        return result