from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def sameDirection(val1: int, val2: int) -> bool:
            return (val1 > 0 and val2 > 0) or (val1 < 0 and val2 < 0)

        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = i

            while True:
                # Move slow pointer one step
                slow = (slow + nums[slow]) % n
                if nums[slow] == 0:
                    break

                # Move fast pointer one step
                fast = (fast + nums[fast]) % n
                if nums[fast] == 0:
                    break

                # Move fast pointer another step
                fast = (fast + nums[fast]) % n
                if nums[fast] == 0:
                    break

                # Check if slow and fast elements are moving in the same direction as the start element
                if not sameDirection(nums[slow], nums[i]) or not sameDirection(nums[fast], nums[i]):
                    break

                if slow == fast:
                    # Check for single-element loop
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

            # Mark all elements visited in this iteration as 0 to avoid re-processing
            idx = i
            val = nums[i]
            while sameDirection(nums[idx], val):
                next_idx = (idx + nums[idx]) % n
                nums[idx] = 0
                idx = next_idx
                if idx == i:
                    break

        return False