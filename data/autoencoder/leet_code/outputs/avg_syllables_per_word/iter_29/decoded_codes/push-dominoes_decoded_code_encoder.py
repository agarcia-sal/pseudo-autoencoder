class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        length_of_dominoes = len(dominoes)
        list_of_forces = [0] * length_of_dominoes

        force_magnitude = 0
        for index in range(length_of_dominoes):
            if dominoes[index] == 'R':
                force_magnitude = length_of_dominoes
            elif dominoes[index] == 'L':
                force_magnitude = 0
            else:
                force_magnitude = max(force_magnitude - 1, 0)
            list_of_forces[index] += force_magnitude

        force_magnitude = 0
        for index in range(length_of_dominoes - 1, -1, -1):
            if dominoes[index] == 'L':
                force_magnitude = length_of_dominoes
            elif dominoes[index] == 'R':
                force_magnitude = 0
            else:
                force_magnitude = max(force_magnitude - 1, 0)
            list_of_forces[index] -= force_magnitude

        list_of_results = []
        for force_value in list_of_forces:
            if force_value > 0:
                list_of_results.append('R')
            elif force_value < 0:
                list_of_results.append('L')
            else:
                list_of_results.append('.')

        return ''.join(list_of_results)