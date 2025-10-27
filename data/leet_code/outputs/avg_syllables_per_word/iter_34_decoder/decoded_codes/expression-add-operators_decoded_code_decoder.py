class Solution:
    def addOperators(self, num: str, target: int):
        def dfs(index, path, value, prev):
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for i in range(index + 1, len(num) + 1):
                operand = num[index:i]
                if len(operand) > 1 and operand[0] == '0':
                    continue

                operand_int = int(operand)

                if index == 0:
                    dfs(i, operand, operand_int, operand_int)
                else:
                    dfs(i, path + "+" + operand, value + operand_int, operand_int)
                    dfs(i, path + "-" + operand, value - operand_int, -operand_int)
                    dfs(i, path + "*" + operand, value - prev + prev * operand_int, prev * operand_int)

        result = []
        dfs(0, "", 0, 0)
        return result