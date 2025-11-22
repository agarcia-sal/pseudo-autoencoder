from collections import Counter, deque

class Solution:
    def minStickers(self, stickers, target):
        stickers = [Counter(s) for s in stickers]
        stickers.sort(key=lambda x: -max(x.values()))

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used = queue.popleft()
            for sticker in stickers:
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