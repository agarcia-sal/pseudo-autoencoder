def maximum_swap(num: int) -> int:
    digits = list(map(int, str(num)))
    last = {d: i for i, d in enumerate(digits)}

    for i, d in enumerate(digits):
        for d2 in range(9, d, -1):
            if last.get(d2, -1) > i:
                digits[i], digits[last[d2]] = digits[last[d2]], digits[i]
                return int("".join(map(str, digits)))
    return num