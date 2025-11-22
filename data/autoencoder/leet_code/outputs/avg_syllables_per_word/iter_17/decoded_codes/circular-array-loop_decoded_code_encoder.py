from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def sameDirection(val1: int, val2: int) -> bool:
            return (val1 > 0 and val2 > 0) or (val1 < 0 and val2 < 0)

        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i
            while True:
                # Move slow pointer one step
                slow = (slow + nums[slow]) % n
                # Move fast pointer one step twice (two steps)
                fast = (fast + nums[fast]) % n
                fast = (fast + nums[fast]) % n

                # Check direction consistency
                if not sameDirection(nums[slow], nums[i]) or not sameDirection(nums[fast], nums[i]):
                    break

                if slow == fast:
                    # Check for cycle of length 1
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

        return False