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
                fast = (fast + nums[fast]) % n
                fast = (fast + nums[fast]) % n

                if not (sameDirection(nums[slow], nums[i]) and sameDirection(nums[fast], nums[i])):
                    break

                if slow == fast:
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

            # mark all nodes in this cycle as 0 to prevent reprocessing
            slow = i
            val = nums[i]
            while sameDirection(nums[slow], val):
                nxt = (slow + nums[slow]) % n
                nums[slow] = 0
                slow = nxt

        return False