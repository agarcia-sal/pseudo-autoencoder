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
                slow_next = (slow + nums[slow]) % n
                if slow_next < 0:
                    slow_next += n

                # Move fast pointer one step
                fast_next = (fast + nums[fast]) % n
                if fast_next < 0:
                    fast_next += n
                # Move fast pointer second step
                fast_next_next = (fast_next + nums[fast_next]) % n
                if fast_next_next < 0:
                    fast_next_next += n

                # Check if nums[slow_next] and nums[i] have the same direction
                if not sameDirection(nums[slow_next], nums[i]) or not sameDirection(nums[fast_next_next], nums[i]):
                    break

                slow = slow_next
                fast = fast_next_next

                if slow == fast:
                    # Check for single-element loop
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

            # Mark all nodes along the way as 0 to avoid reprocessing
            # This optimization prevent repeated work
            marker = i
            direction = nums[i]
            while nums[marker] != 0 and sameDirection(nums[marker], direction):
                next_marker = (marker + nums[marker]) % n
                nums[marker] = 0
                marker = next_marker

        return False