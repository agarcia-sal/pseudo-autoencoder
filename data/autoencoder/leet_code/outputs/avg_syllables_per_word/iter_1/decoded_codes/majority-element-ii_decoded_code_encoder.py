def majority_element(nums):
    n1, n2 = 0, 0
    m1, m2 = 0, 1
    for num in nums:
        if num == m1:
            n1 += 1
        elif num == m2:
            n2 += 1
        elif n1 == 0:
            m1, n1 = num, 1
        elif n2 == 0:
            m2, n2 = num, 1
        else:
            n1 -= 1
            n2 -= 1
    return [x for x in (m1, m2) if nums.count(x) > len(nums) // 3]