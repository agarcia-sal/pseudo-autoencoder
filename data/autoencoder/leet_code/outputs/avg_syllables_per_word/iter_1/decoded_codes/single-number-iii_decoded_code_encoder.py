def single_number(nums):
    xor_all = 0
    for n in nums:
        xor_all ^= n
    diff_bit = xor_all & -xor_all
    num1 = num2 = 0
    for n in nums:
        if n & diff_bit:
            num1 ^= n
        else:
            num2 ^= n
    return [num1, num2]