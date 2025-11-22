class Solution:
    def circularArrayLoop(self, nums):
        def sameDirection(val1, val2):
            # Returns True if both values have the same sign (both positive or both negative)
            return (val1 > 0 and val2 > 0) or (val1 < 0 and val2 < 0)

        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i

            while True:
                # Move slow pointer one step
                slow = (slow + nums[slow]) % n
                if nums[slow] == 0:
                    break  # visited or zeroed, no loop

                # Move fast pointer one step
                fast = (fast + nums[fast]) % n
                if nums[fast] == 0:
                    break

                # Move fast pointer second step
                fast = (fast + nums[fast]) % n
                if nums[fast] == 0:
                    break

                # If directions differ, break
                if not sameDirection(nums[slow], nums[i]) or not sameDirection(nums[fast], nums[i]):
                    break

                if slow == fast:
                    # Check for single-element cycle
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

            # Mark all elements in the current sequence as 0 to avoid revisiting
            j = i
            val = nums[i]
            while sameDirection(nums[j], val):
                next_j = (j + nums[j]) % n
                nums[j] = 0
                j = next_j

        return False