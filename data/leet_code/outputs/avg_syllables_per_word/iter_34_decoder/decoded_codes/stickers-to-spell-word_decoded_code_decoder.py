from collections import Counter, deque

class Solution:
    def minStickers(self, stickers, target):
        stickers = [Counter(sticker) for sticker in stickers]
        # Sort stickers by the negative of the maximum frequency value to prioritize more useful stickers
        stickers.sort(key=lambda c: -max(c.values()) if c else 0)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            for sticker in stickers:
                if current_target[0] not in sticker:
                    continue
                remaining = Counter(current_target)
                remaining.subtract(sticker)
                # Remove zero or negative counts
                new_target = ''.join(sorted(c * cnt for c, cnt in remaining.items() if cnt > 0))
                if new_target == '':
                    return used_stickers + 1
                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))
        return -1