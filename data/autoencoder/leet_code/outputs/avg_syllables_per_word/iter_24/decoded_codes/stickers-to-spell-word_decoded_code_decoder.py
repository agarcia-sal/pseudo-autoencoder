from collections import Counter, deque

class Solution:
    def minStickers(self, stickers, target):
        stickers = [Counter(sticker) for sticker in stickers]
        stickers.sort(key=lambda x: -max(x.values()) if x else 0)
        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            current_target_counter = Counter(current_target)

            for sticker in stickers:
                if not current_target or current_target[0] not in sticker:
                    continue

                remaining = current_target_counter - sticker
                if not remaining:
                    return used_stickers + 1

                new_target = ''.join(sorted(remaining.elements()))
                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1