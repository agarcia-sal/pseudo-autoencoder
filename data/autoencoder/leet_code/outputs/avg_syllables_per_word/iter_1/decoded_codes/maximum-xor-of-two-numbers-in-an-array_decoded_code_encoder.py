max_xor = 0
for i in range(31, -1, -1):
    max_xor <<= 1
    candidate = max_xor | 1
    prefixes = {num >> i for num in nums}
    if any((candidate ^ p) in prefixes for p in prefixes):
        max_xor = candidate
return max_xor