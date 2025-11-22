def max_beauty(flowers, newFlowers, target, full, partial):
    flowers.sort()
    n = len(flowers)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + flowers[i]

    # count of flowers[i] >= target from right
    complete_gardens = 0
    for i in range(n - 1, -1, -1):
        if flowers[i] >= target:
            complete_gardens += 1
        else:
            break

    max_beauty = 0
    current_new_flowers = newFlowers
    for i in range(complete_gardens, n + 1):
        if i > 0:
            current_new_flowers -= (target - flowers[n - i])
        if current_new_flowers < 0:
            break

        left, right = 0, n - i - 1
        while left <= right:
            mid = (left + right) // 2
            cost = flowers[mid] * (mid + 1) - prefix_sum[mid + 1]
            if cost > current_new_flowers:
                right = mid - 1
            else:
                left = mid + 1

        if right >= 0:
            cost = flowers[right] * (right + 1) - prefix_sum[right + 1]
            inc_max = flowers[right] + (current_new_flowers - cost) // (right + 1)
        else:
            inc_max = 0

        inc_max = min(inc_max, target - 1)
        total = i * full + inc_max * partial
        if total > max_beauty:
            max_beauty = total

    return max_beauty