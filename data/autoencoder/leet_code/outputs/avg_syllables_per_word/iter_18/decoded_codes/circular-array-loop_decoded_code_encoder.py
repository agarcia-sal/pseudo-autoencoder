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
                slow = (slow + nums[slow]) % n
                if not sameDirection(nums[slow], nums[i]):
                    break

                fast = (fast + nums[fast]) % n
                if not sameDirection(nums[fast], nums[i]):
                    break

                fast = (fast + nums[fast]) % n
                if not sameDirection(nums[fast], nums[i]):
                    break

                if slow == fast:
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

            # mark all elements traversed in this round as 0 to prevent re-processing
            mark = i
            sign = nums[i]
            while nums[mark] != 0 and sameDirection(nums[mark], sign):
                next_index = (mark + nums[mark]) % n
                nums[mark] = 0
                mark = next_index

        return False