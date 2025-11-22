from collections import Counter, deque

class Solution:
    def minStickers(self, stickers, target):
        frequency_counters = []
        for sticker in stickers:
            frequency_counters.append(Counter(sticker))
        frequency_counters.sort(key=lambda c: -max(c.values()) if c else 0)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            for sticker_frequency in frequency_counters:
                if not current_target or current_target[0] not in sticker_frequency:
                    continue

                remaining_frequency = Counter(current_target) - sticker_frequency
                new_target_string = ''.join(sorted(remaining_frequency.elements()))
                if not new_target_string:
                    return used_stickers + 1
                if new_target_string not in memo:
                    memo[new_target_string] = used_stickers + 1
                    queue.append((new_target_string, used_stickers + 1))

        return -1