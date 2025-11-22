from collections import Counter, deque

class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        sticker_counts = [Counter(s) for s in stickers]
        # Sort stickers by the negative of their highest frequency value for early pruning
        sticker_counts.sort(key=lambda c: -max(c.values()) if c else 0)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            current_counter = Counter(current_target)

            for sticker in sticker_counts:
                if current_target[0] not in sticker:  # quickly skip if first char not in sticker
                    continue

                remaining = current_counter - sticker
                new_target = ''.join(sorted(remaining.elements()))

                if not new_target:
                    return used_stickers + 1

                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))
        return -1