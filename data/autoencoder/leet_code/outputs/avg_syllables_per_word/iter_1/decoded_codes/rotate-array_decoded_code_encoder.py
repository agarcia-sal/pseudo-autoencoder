n = len(nums)
k = k % n

def reverse(s, e):
    while s < e:
        nums[s], nums[e] = nums[e], nums[s]
        s += 1
        e -= 1

reverse(0, n-1)
reverse(0, k-1)
reverse(k, n-1)