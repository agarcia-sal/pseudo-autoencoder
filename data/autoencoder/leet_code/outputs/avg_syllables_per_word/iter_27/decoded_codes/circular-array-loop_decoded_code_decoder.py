from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def sameDirection(val1: int, val2: int) -> bool:
            return (val1 > 0 and val2 > 0) or (val1 < 0 and val2 < 0)

        n = len(nums)
        if n < 2:
            return False

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = i

            while True:
                # Move slow pointer one step
                slow = (slow + nums[slow]) % n
                # Move fast pointer one step
                fast = (fast + nums[fast]) % n
                # Move fast pointer another step
                fast = (fast + nums[fast]) % n

                if not (sameDirection(nums[slow], nums[i]) and sameDirection(nums[fast], nums[i])):
                    break

                if slow == fast:
                    # Check for single-element loop
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

        return False