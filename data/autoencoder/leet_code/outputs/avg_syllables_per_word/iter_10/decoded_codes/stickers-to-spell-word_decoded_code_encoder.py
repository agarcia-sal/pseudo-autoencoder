from collections import Counter, deque

class Solution:
    def minStickers(self, stickers, target):
        sticker_counts = [Counter(sticker) for sticker in stickers]
        sticker_counts.sort(key=lambda c: -max(c.values()))

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used = queue.popleft()
            for sticker in sticker_counts:
                if current_target[0] not in sticker:
                    continue
                remaining = Counter(current_target) - sticker
                new_target = ''.join(sorted(remaining.elements()))
                if not new_target:
                    return used + 1
                if new_target not in memo:
                    memo[new_target] = used + 1
                    queue.append((new_target, used + 1))
        return -1