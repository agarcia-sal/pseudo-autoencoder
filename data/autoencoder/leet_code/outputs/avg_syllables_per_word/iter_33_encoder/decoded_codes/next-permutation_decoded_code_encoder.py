class Solution:
    def nextPermutation(self, nums) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap_elements_at_positions(nums, i, j)
        self.reverse_subsequence_starting_at_position(nums, i + 1)

    def swap_elements_at_positions(self, nums, position_one, position_two) -> None:
        nums[position_one], nums[position_two] = nums[position_two], nums[position_one]

    def reverse_subsequence_starting_at_position(self, nums, start_position) -> None:
        end_position = len(nums) - 1
        while start_position < end_position:
            self.swap_elements_at_positions(nums, start_position, end_position)
            start_position += 1
            end_position -= 1