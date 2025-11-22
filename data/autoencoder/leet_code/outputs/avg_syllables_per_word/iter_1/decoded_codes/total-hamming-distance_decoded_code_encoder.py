def totalHammingDistance(nums):
    total = 0
    for i in range(32):
        c1 = sum((num >> i) & 1 for num in nums)
        c0 = len(nums) - c1
        total += c1 * c0
    return total