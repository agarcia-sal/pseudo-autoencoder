class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # Cap n at 6 according to the given complex expression
        n = n if n <= 6 else 6

        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            if presses == 1:
                return 3
            else:
                return 4
        if presses == 1:
            return 4
        if presses == 2:
            return 7
        return 8