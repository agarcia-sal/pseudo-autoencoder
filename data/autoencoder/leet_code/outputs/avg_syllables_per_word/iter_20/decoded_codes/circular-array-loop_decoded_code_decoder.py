class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        def sameDirection(val1: int, val2: int) -> bool:
            return (val1 > 0 and val2 > 0) or (val1 < 0 and val2 < 0)

        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i

            while True:
                # Move slow pointer by 1 step
                slow = (slow + nums[slow]) % n
                # Move fast pointer by 1 step
                fast = (fast + nums[fast]) % n
                # Move fast pointer by another 1 step (total 2 steps)
                fast = (fast + nums[fast]) % n

                # Check direction consistency
                if not sameDirection(nums[slow], nums[i]) or not sameDirection(nums[fast], nums[i]):
                    break

                # Check if pointers meet
                if slow == fast:
                    # Check for single-element loop, which is invalid
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

            # Mark all elements in the traversed cycle as 0 to avoid reprocessing
            marker = i
            val = nums[i]
            while sameDirection(nums[marker], val):
                nxt = (marker + nums[marker]) % n
                nums[marker] = 0
                marker = nxt
                if marker == i:
                    break

        return False