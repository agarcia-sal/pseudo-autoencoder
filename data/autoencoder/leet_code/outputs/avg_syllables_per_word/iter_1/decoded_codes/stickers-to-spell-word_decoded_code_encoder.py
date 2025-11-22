from collections import Counter, deque

def minStickers(stickers, target):
    # Convert stickers to char frequency counters
    sticker_counts = [Counter(sticker) for sticker in stickers]
    # Sort stickers by max freq descending
    sticker_counts.sort(key=lambda c: max(c.values()) if c else 0, reverse=True)

    queue = deque()
    queue.append((target, 0))
    memo = {target: 0}

    while queue:
        cur, used = queue.popleft()
        cur_counter = Counter(cur)

        for sticker in sticker_counts:
            # If first char of cur not in sticker, continue
            if cur[0] not in sticker:
                continue

            # Rem = cur_counter - sticker
            rem = cur_counter - sticker

            # new_t = sorted string from rem
            new_t = ''.join(sorted(rem.elements()))

            if not new_t:
                return used + 1

            if new_t not in memo:
                memo[new_t] = used + 1
                queue.append((new_t, used + 1))

    return -1