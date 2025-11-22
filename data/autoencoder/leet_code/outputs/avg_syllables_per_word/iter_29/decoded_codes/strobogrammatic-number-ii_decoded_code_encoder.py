class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        zero, one = 0, 1

        def dfs(u: int) -> list[str]:
            if u == zero:
                return [""]
            if u == one:
                return ["0", "1", "8"]

            answer_list = []
            for v in dfs(u - 2):
                for left_character, right_character in [("1", "1"), ("8", "8"), ("6", "9"), ("9", "6")]:
                    answer_list.append(left_character + v + right_character)
                if u != n:
                    answer_list.append("0" + v + "0")
            return answer_list

        return dfs(n)