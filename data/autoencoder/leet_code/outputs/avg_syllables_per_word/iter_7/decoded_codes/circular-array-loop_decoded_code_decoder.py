from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def sameDirection(val1: int, val2: int) -> bool:
            return (val1 > 0 and val2 > 0) or (val1 < 0 and val2 < 0)

        n = len(nums)

        for i in range(n):
            slow = i
            fast = i

            if nums[i] == 0:
                continue

            while True:
                slow = (slow + nums[slow]) % n
                if slow < 0:
                    slow += n

                fast = (fast + nums[fast]) % n
                if fast < 0:
                    fast += n

                fast = (fast + nums[fast]) % n
                if fast < 0:
                    fast += n

                if not sameDirection(nums[slow], nums[i]) or not sameDirection(nums[fast], nums[i]):
                    break

                if slow == fast:
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

        return False