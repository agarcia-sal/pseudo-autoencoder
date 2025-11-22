class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        minimum_window_length = float('inf')
        minimum_window_start_index = -1
        length_of_s1 = len(s1)
        length_of_s2 = len(s2)

        for index_i in range(length_of_s1):
            pointer_j = 0
            for index_k in range(index_i, length_of_s1):
                if s1[index_k] == s2[pointer_j]:
                    pointer_j += 1
                    if pointer_j == length_of_s2:
                        window_length = index_k - index_i + 1
                        if window_length < minimum_window_length:
                            minimum_window_length = window_length
                            minimum_window_start_index = index_i
                        break

        if minimum_window_start_index == -1:
            return ""
        else:
            return s1[minimum_window_start_index:minimum_window_start_index + minimum_window_length]