from collections import Counter, deque

class Solution:
    def minStickers(self, stickers, target):
        stickers_freq = [Counter(sticker) for sticker in stickers]
        stickers_freq.sort(key=lambda x: -max(x.values(), default=0))

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()

            for sticker in stickers_freq:
                if current_target[0] not in sticker:
                    continue

                remaining = Counter(current_target) - sticker
                new_target = ''.join(sorted(remaining.elements()))

                if not new_target:
                    return used_stickers + 1
                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1