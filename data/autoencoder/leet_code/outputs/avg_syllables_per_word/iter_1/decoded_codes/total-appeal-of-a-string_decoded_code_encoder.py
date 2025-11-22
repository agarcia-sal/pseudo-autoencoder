def calculate_total(s: str) -> int:
    last = [-1] * 26
    total = 0
    curr = 0
    for i, c in enumerate(s):
        idx = ord(c) - ord('a')
        curr += i - last[idx]
        total += curr
        last[idx] = i
    return total