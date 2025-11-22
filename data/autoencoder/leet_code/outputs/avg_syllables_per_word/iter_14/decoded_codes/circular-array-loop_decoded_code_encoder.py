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

                # Check directions consistency
                if not sameDirection(nums[slow], nums[i]) or not sameDirection(nums[fast], nums[i]):
                    break

                if slow == fast:
                    # Check for single-element cycle
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

            # Mark all elements in the current traversal as 0 to avoid revisiting
            mark = i
            val = nums[i]
            while nums[mark] != 0 and sameDirection(nums[mark], val):
                next_index = (mark + nums[mark]) % n
                nums[mark] = 0  # Mark visited
                mark = next_index

        return False