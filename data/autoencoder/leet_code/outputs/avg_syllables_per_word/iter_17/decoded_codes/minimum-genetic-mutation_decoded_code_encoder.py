from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        set_of_bank_sequences = set(bank)
        queue = deque([(start, 0)])
        mutation_map = {
            'A': 'TCG',
            'T': 'ACG',
            'C': 'ATG',
            'G': 'ATC'
        }
        while queue:
            current_sequence, current_step = queue.popleft()
            if current_sequence == end:
                return current_step
            for index, character in enumerate(current_sequence):
                for possible_mutation in mutation_map[character]:
                    next_sequence = current_sequence[:index] + possible_mutation + current_sequence[index+1:]
                    if next_sequence in set_of_bank_sequences:
                        queue.append((next_sequence, current_step + 1))
                        set_of_bank_sequences.remove(next_sequence)
        return -1