def min_number_after_k_swaps(num: str, k: int) -> str:
    num = list(num)
    n = len(num)
    while k > 0:
        swapped = False
        for i in range(n - 1):
            if num[i] > num[i + 1]:
                min_digit = '9'
                min_index = -1
                for j in range(i, min(i + k + 1, n)):
                    if num[j] < min_digit:
                        min_digit = num[j]
                        min_index = j
                # Rotate num[i..min_index] to put num[min_index] at position i
                if min_index > i:
                    temp = num[min_index]
                    for x in range(min_index, i, -1):
                        num[x] = num[x - 1]
                    num[i] = temp
                    k -= (min_index - i)
                swapped = True
                break
        if not swapped:
            break
    return ''.join(num)