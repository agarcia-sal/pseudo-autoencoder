class Solution:
    def validSubarrays(self, nums: list[int]) -> int:
        stack = []
        count = 0

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(num)
            count += len(stack)

        return count