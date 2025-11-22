from typing import List

class Solution:
    def canPartitionKSubsets(self, list_of_numbers: List[int], number_of_subsets: int) -> bool:
        total_sum = sum(list_of_numbers)
        if total_sum % number_of_subsets != 0:
            return False
        target_value = total_sum // number_of_subsets
        list_of_numbers.sort(reverse=True)

        def can_partition(current_index: int, remaining_subsets: int, current_subset_sum: int, usage_list: List[bool]) -> bool:
            if remaining_subsets == 0:
                return True
            if current_subset_sum == target_value:
                return can_partition(0, remaining_subsets - 1, 0, usage_list)

            for iterator in range(current_index, len(list_of_numbers)):
                if not usage_list[iterator] and current_subset_sum + list_of_numbers[iterator] <= target_value:
                    usage_list[iterator] = True
                    if can_partition(iterator + 1, remaining_subsets, current_subset_sum + list_of_numbers[iterator], usage_list):
                        return True
                    usage_list[iterator] = False
            return False

        usage_list = [False] * len(list_of_numbers)
        return can_partition(0, number_of_subsets, 0, usage_list)