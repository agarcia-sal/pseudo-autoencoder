class Solution:
    def splitIntoFibonacci(self, num_string: str) -> list[int]:
        def backtrack(start_position: int, current_path: list[int]) -> list[int]:
            if start_position == len(num_string) and len(current_path) >= 3:
                return current_path
            for end_position in range(start_position + 1, len(num_string) + 1):
                if num_string[start_position] == '0' and end_position > start_position + 1:
                    continue
                next_number = int(num_string[start_position:end_position])
                if next_number >= 2**31:
                    break
                if len(current_path) < 2 or next_number == current_path[-1] + current_path[-2]:
                    result = backtrack(end_position, current_path + [next_number])
                    if result:
                        return result
            return []
        return backtrack(0, [])