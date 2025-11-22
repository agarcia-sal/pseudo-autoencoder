def largest_multiple_of_3(digits):
    from collections import Counter

    count = Counter(digits)
    total = sum(d * count[d] for d in count)
    r = total % 3

    def remove_digits(targets, number):
        removed = 0
        for d in targets:
            while count[d] > 0 and removed < number:
                count[d] -= 1
                removed += 1
            if removed == number:
                return True
        return removed == number

    if r == 1:
        if not remove_digits([1,4,7], 1):
            remove_digits([2,5,8], 2)
    elif r == 2:
        if not remove_digits([2,5,8], 1):
            remove_digits([1,4,7], 2)

    result = ''.join(str(d) * count[d] for d in range(9, -1, -1))
    if result == "" or result[0] == "0":
        return "0"
    return result