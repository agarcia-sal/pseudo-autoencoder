class Solution:
    def addOperators(self, num, target):
        def dfs(index, path, value, prev):
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for i in range(index + 1, len(num) + 1):
                operand = num[index:i]
                if len(operand) > 1 and operand[0] == '0':
                    continue

                operand_val = int(operand)
                if index == 0:
                    dfs(i, operand, operand_val, operand_val)
                else:
                    dfs(i, path + '+' + operand, value + operand_val, operand_val)
                    dfs(i, path + '-' + operand, value - operand_val, -operand_val)
                    dfs(i, path + '*' + operand, value - prev + prev * operand_val, prev * operand_val)

        result = []
        dfs(0, '', 0, 0)
        return result