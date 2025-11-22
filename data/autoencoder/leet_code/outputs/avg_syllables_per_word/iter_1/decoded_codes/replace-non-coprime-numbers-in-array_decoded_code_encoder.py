from math import gcd

def process_nums(nums):
    S = []
    for num in nums:
        while S:
            g = gcd(S[-1], num)
            if g == 1:
                break
            num = (S[-1] * num) // g
            S.pop()
        S.append(num)
    return S