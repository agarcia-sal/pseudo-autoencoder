class Solution:
    def reversePairs(self, nums):
        def merge_and_count(nums, start_index, end_index):
            if start_index >= end_index:
                return 0

            middle_index = (start_index + end_index) // 2
            total_count = merge_and_count(nums, start_index, middle_index) + merge_and_count(nums, middle_index + 1, end_index)

            second_pointer = middle_index + 1
            for current_index in range(start_index, middle_index + 1):
                while second_pointer <= end_index and nums[current_index] > 2 * nums[second_pointer]:
                    second_pointer += 1
                total_count += second_pointer - (middle_index + 1)

            merged_list = []
            left_pointer, right_pointer = start_index, middle_index + 1

            while left_pointer <= middle_index and right_pointer <= end_index:
                if nums[left_pointer] <= nums[right_pointer]:
                    merged_list.append(nums[left_pointer])
                    left_pointer += 1
                else:
                    merged_list.append(nums[right_pointer])
                    right_pointer += 1

            merged_list.extend(nums[left_pointer:middle_index + 1])
            merged_list.extend(nums[right_pointer:end_index + 1])

            nums[start_index:end_index + 1] = merged_list

            return total_count

        return merge_and_count(nums, 0, len(nums) - 1)