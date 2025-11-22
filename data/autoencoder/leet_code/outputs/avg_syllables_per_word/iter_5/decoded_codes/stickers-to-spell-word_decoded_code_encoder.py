from collections import Counter, deque

class Solution:
    def minStickers(self, stickers, target):
        stickers = [Counter(s) for s in stickers]
        stickers.sort(key=lambda c: -max(c.values()) if c else 0)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used = queue.popleft()
            curr_counter = Counter(current_target)

            for sticker in stickers:
                if sticker[current_target[0]] == 0:
                    continue
                remaining = curr_counter - sticker
                if not remaining:
                    return used + 1

                new_target = ''.join(sorted(remaining.elements()))
                if new_target not in memo:
                    memo[new_target] = used + 1
                    queue.append((new_target, used + 1))

        return -1