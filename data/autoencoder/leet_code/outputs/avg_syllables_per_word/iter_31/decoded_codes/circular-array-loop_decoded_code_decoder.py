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

                # Move fast pointer one step
                fast = (fast + nums[fast]) % n
                # Move fast pointer another step
                fast = (fast + nums[fast]) % n

                if not sameDirection(nums[slow], nums[i]) or not sameDirection(nums[fast], nums[i]):
                    break

                if slow == fast:
                    # Check for cycle length > 1
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

            # Mark all nodes on the current path as 0 to avoid rechecking
            marker = i
            val = nums[i]
            while nums[marker] != 0 and sameDirection(nums[marker], val):
                next_index = (marker + nums[marker]) % n
                nums[marker] = 0
                marker = next_index

        return False