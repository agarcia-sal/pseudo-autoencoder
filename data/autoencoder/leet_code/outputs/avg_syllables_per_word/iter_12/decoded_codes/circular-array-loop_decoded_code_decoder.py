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
                # Move slow pointer one step
                slow = (slow + nums[slow]) % n
                # Move fast pointer one step
                fast = (fast + nums[fast]) % n
                # Move fast pointer second step
                fast = (fast + nums[fast]) % n

                if not sameDirection(nums[slow], nums[i]) or not sameDirection(nums[fast], nums[i]):
                    break

                if slow == fast:
                    # Check for loop length more than 1
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

            # Mark all nodes visited in this iteration as 0 to avoid revisiting
            marker = i
            direction = nums[i]
            while sameDirection(nums[marker], direction):
                next_marker = (marker + nums[marker]) % n
                nums[marker] = 0
                marker = next_marker

        return False