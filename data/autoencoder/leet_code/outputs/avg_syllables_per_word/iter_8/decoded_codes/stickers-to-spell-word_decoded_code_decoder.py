from collections import deque, Counter

class Solution:
    def minStickers(self, stickers, target):
        stickers_freq = []
        for sticker in stickers:
            freq = Counter(sticker)
            stickers_freq.append(freq)

        stickers_freq.sort(key=lambda f: max(f.values()) if f else 0, reverse=True)

        queue = deque()
        queue.append((target, 0))
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            current_counter = Counter(current_target)

            for sticker in stickers_freq:
                if current_target[0] not in sticker:
                    continue

                remaining = current_counter.copy()
                for ch in sticker:
                    if ch in remaining:
                        remaining[ch] -= sticker[ch]
                        if remaining[ch] <= 0:
                            del remaining[ch]

                new_target = ''.join(sorted(remaining.elements()))

                if not new_target:
                    return used_stickers + 1

                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1