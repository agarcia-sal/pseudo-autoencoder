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
                # move slow pointer one step
                slow = (slow + nums[slow]) % n
                # adjust if negative after modulo
                if slow < 0:
                    slow += n

                # move fast pointer one step
                fast = (fast + nums[fast]) % n
                if fast < 0:
                    fast += n
                # move fast pointer second step
                fast = (fast + nums[fast]) % n
                if fast < 0:
                    fast += n

                if (
                    not sameDirection(nums[slow], nums[i]) or 
                    not sameDirection(nums[fast], nums[i])
                ):
                    break

                if slow == fast:
                    # check for cycle of length 1
                    next_pos = (slow + nums[slow]) % n
                    if next_pos == slow:
                        break
                    return True

        return False