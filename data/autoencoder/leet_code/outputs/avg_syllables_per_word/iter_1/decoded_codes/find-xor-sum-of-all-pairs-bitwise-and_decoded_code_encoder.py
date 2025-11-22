def xor_and(arr1, arr2):
    xor1 = 0
    for num in arr1:
        xor1 ^= num
    xor2 = 0
    for num in arr2:
        xor2 ^= num
    return xor1 & xor2