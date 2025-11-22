def min_waste(packages, boxes):
    packages.sort()
    n = len(packages)
    prefix_sum = [0]
    for p in packages:
        prefix_sum.append(prefix_sum[-1] + p)

    min_waste = float('inf')
    for box_list in boxes:
        box_list.sort()
        if box_list[-1] < packages[-1]:
            continue
        total_waste = 0
        last = 0
        for box_size in box_list:
            index = last
            while index < n and packages[index] <= box_size:
                index += 1
            if index > last:
                total_waste += (index - last) * box_size - (prefix_sum[index] - prefix_sum[last])
                last = index
            if last == n:
                break
        if last == n:
            min_waste = min(min_waste, total_waste)

    return min_waste % 1_000_000_007 if min_waste != float('inf') else -1