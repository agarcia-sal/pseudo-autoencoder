class Solution:
    def pushDominoes(self, dominoes_string: str) -> str:
        n = len(dominoes_string)
        forces = [0] * n

        force = 0
        for i in range(n):
            if dominoes_string[i] == 'R':
                force = n
            elif dominoes_string[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes_string[i] == 'L':
                force = n
            elif dominoes_string[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return ''.join(result)