from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence_dictionary = self.create_last_occurrence_dictionary(s)
        start_index = 0
        end_index = 0
        partition_sizes_list = []
        for index, character in enumerate(s):
            end_index = max(end_index, last_occurrence_dictionary[character])
            if index == end_index:
                partition_size = end_index - start_index + 1
                partition_sizes_list.append(partition_size)
                start_index = index + 1
        return partition_sizes_list

    def create_last_occurrence_dictionary(self, s: str) -> dict:
        last_occurrence = {}
        for index, character in enumerate(s):
            last_occurrence[character] = index
        return last_occurrence