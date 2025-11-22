map = {}
for a in nums1:
    for b in nums2:
        map[a+b] = map.get(a+b, 0) + 1

count = 0
for c in nums3:
    for d in nums4:
        count += map.get(-(c+d), 0)

return count