def circularArrayLoop(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            continue
        slow, fast = i, i
        while True:
            slow = (slow + nums[slow]) % n
            fast = (fast + nums[fast]) % n
            fast = (fast + nums[fast]) % n

            if nums[slow] * nums[i] <= 0 or nums[fast] * nums[i] <= 0:
                break

            if slow == fast:
                if slow == (slow + nums[slow]) % n:
                    break
                return True
    return False