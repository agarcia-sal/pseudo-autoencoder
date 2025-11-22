class Solution:
    def circularArrayLoop(self, nums):
        def sameDirection(val1, val2):
            return (val1 > 0 and val2 > 0) or (val1 < 0 and val2 < 0)

        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i

            while True:
                slow = (slow + nums[slow]) % n
                if nums[slow] == 0 or not sameDirection(nums[slow], nums[i]):
                    break

                fast = (fast + nums[fast]) % n
                if nums[fast] == 0 or not sameDirection(nums[fast], nums[i]):
                    break

                fast = (fast + nums[fast]) % n
                if nums[fast] == 0 or not sameDirection(nums[fast], nums[i]):
                    break

                if slow == fast:
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

            # Mark all elements in the current path as 0 to avoid reprocessing
            pos = i
            val = nums[i]
            while nums[pos] != 0 and sameDirection(nums[pos], val):
                nxt = (pos + nums[pos]) % n
                nums[pos] = 0
                pos = nxt

        return False