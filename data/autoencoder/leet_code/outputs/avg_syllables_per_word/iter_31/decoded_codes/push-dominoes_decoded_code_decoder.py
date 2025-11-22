from typing import List

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces: List[int] = [0] * n

        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = force - 1 if force > 0 else 0
            forces[i] += force

        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = force - 1 if force > 0 else 0
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